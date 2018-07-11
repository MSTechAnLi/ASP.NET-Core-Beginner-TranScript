using System;
using System.IO;

namespace FileC
{
    class Program
    {
        static void Main(string[] args)
        {
            Merge();
            DeleSpace();
        }
        public static Merge()//负责合并中英文txt文件
        {
            string line1,line2,
                   usFile=@"英文txt文件路径",
                   znFile=@"中文txt文件路径";
            StreamReader file1,file2;
            StreamWriter file3 = new StreamWriter(@"输出文件路径");

            file1 = new StreamReader(usFile);
            file2 = new StreamReader(znFile);  

            while(((line1 = file1.ReadLine()) != null)&&(line2 = file2.ReadLine()) != null)
            {  
                file3.WriteLine(line1);
                file3.WriteLine(line2);
            }  

            file1.Close();
            file2.Close();
            file3.Close();
        }
        public static DeleSpace()//删除初步编辑后的空格
        {
            int count = 0;
            string line;
            StreamReader in = new StreamReader(@"输入文件路径");
            StreamWriter out = new StreamWriter(@"输出文件路径");

            while(count<10){
                line = in.ReadLine();
                if((line!="")&&(line!=null))
                {
                    out.WriteLine(line);
                    count = 0;
                }else{
                    count++;
                }
            }
            file1.Close();
            file2.Close();
        }
    }
}
