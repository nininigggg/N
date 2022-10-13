import xmind
import os
import shutil
import zipfile
from openpyxl import load_workbook

file_path = os.path.dirname(os.path.realpath(__file__))


class convert:
    def extract(self, d_path, f_path):
        """
        zip解压缩乱码问题处理
        :param d_path:
        :param f_path:
        :return:
        """
        global zf
        # os.chdir(root_path)
        root = d_path
        if not os.path.exists(root):
            os.makedirs(root)
        # print('ffff',os.getcwd())
        zf = zipfile.ZipFile(f_path, "r")

        for n in zf.infolist():
            srcName = n.filename
            try:
                decodeName = srcName.encode("cp437").decode("utf-8")
            except:
                try:
                    decodeName = srcName.encode("cp437").decode("gbk")
                except:
                    decodeName = srcName
            spiltArr = decodeName.split("/")
            path = root
            for temp in spiltArr:
                path = os.path.join(path, temp)

            if decodeName.endswith("/"):
                if not os.path.exists(path):
                    os.makedirs(path)
            else:
                if not os.path.exists(os.path.dirname(path)):
                    os.makedirs(os.path.dirname(path))
                f = open(path, "wb")
                f.write(zf.read(srcName))
                f.close()
        zf.close()

    # 修复无法打开xmind文件的问题
    def aftertreatment(self, path):

        # 修改名字
        retval = os.path.dirname(os.path.abspath(__file__))
        folder = os.path.dirname(path)
        name = os.path.basename(path)
        unzip_folder = os.path.splitext(name)[0]
        zip_name = unzip_folder + ".zip"
        os.chdir(folder)
        os.rename(name, zip_name)
        os.chdir(retval)
        # 解压
        unzip_path = os.path.join(folder, unzip_folder)
        if not os.path.exists(unzip_path):
            os.mkdir(unzip_path)

        inf_folder = os.path.join(unzip_path, "META-INF")
        if not os.path.exists(inf_folder):
            os.mkdir(inf_folder)

        self.extract(unzip_path, os.path.join(folder, zip_name))
        shutil.copyfile("./main_fest.xml", os.path.join(inf_folder, "manifest.xml"))
        os.remove(os.path.join(folder, zip_name))
        shutil.make_archive(unzip_path, 'zip', unzip_path)
        file_path = unzip_path + '.zip'
        # print(file_path)
        os.chdir(os.path.dirname(file_path))
        os.rename(os.path.basename(file_path), name)
        os.chdir(retval)
        shutil.rmtree(unzip_path)

    # 转化成xmind文件
    def gen_xmind_file(self, xls):
        global sub_topic
        readbook = load_workbook(xls)
        # readbook = xlrd.open_workbook(xls)
        # count_sheets = len(readbook.sheets())
        sheet_list = readbook.get_sheet_names()
        count_sheets = len(sheet_list)
        try:
            for i in range(count_sheets):
                # sheet = readbook.sheet_by_index(i)
                sheet_name = sheet_list[i]
                workbook = xmind.load(sheet_name + '.xmind')

                first_sheet = workbook.getPrimarySheet()
                # 根节点
                root_topic = first_sheet.getRootTopic()
                root_topic.setTitle(sheet_name)
                sheet = readbook.get_sheet_by_name(sheet_name)

                for row in list(sheet.rows)[1:]:
                    for c in range(len(row)):
                        m = 0
                        value = row[c].value
                        if c == 0:
                            if len(root_topic.getSubTopics()) == 0:
                                sub_topic = root_topic.addSubTopic()
                                sub_topic.setTitle(value)
                            else:
                                for j in root_topic.getSubTopics():
                                    m += 1
                                    if value == j.getTitle():
                                        sub_topic = j
                                        break
                                    elif m == len(root_topic.getSubTopics()):
                                        sub_topic = root_topic.addSubTopic()
                                        sub_topic.setTitle(value)
                        else:
                            if len(sub_topic.getSubTopics()) == 0:
                                sub_topic = sub_topic.addSubTopic()
                                sub_topic.setTitle(value)
                            else:
                                for k in sub_topic.getSubTopics():
                                    m += 1
                                    if value == k.getTitle():
                                        sub_topic = k
                                        break
                                    elif m == len(sub_topic.getSubTopics()):
                                        sub_topic = sub_topic.addSubTopic()
                                        sub_topic.setTitle(value)
                xmind.save(workbook, path=sheet_name + '.xmind')
                # 修复
                self.aftertreatment(r'./' + sheet_name + '.xmind')
            return 'OK'
        except:
            pass


if __name__ == '__main__':
    convert().gen_xmind_file(xls=r'./统一运营作业用例导出.xlsx')
