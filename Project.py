import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame()
csv_file = "E:\\GitHub\\Result Data Analysis\\Result.csv"

def result_data_analysis():
        df = pd.read_csv(csv_file)
        while 0<1:
            print("                   Result Data Analysis")
            print('*'*60)  
            print("                         Welcome")
            print('*'*60,"\n") 
            print('1.  Displaying all information of Dataframe.\n')
            print('2.  Displaying only column names of imported CSV.\n')
            print('3.  Adding a new record in Dataframe.\n ')
            print('4.  To show some specific column.\n')
            print('5.  Finding some specific records to be shown.\n')
            print('6.  Displaying information from top and bottom of Dataframe.\n')
            print('7.  Sorting of records in Ascending or Descending orders.\n')
            print('8.  Deleting a column of Dataframe.\n')
            print('9. Row Deletion.\n')
            print('10. Exit from Data Analysis Menu and Go to Graph Menu.\n')
            
            ch = int(input('Enter your choice:'))
            
            if ch == 1:
                print(df)
                print('\n\n\n Press any key to continue....')
                wait = input()
            if ch == 2:
                print(df.columns)
                print('\n\n\n Press any key to continue....')
                wait = input()
            if ch == 3:
                a = int(input('Enter roll number in integers :'))
                b = input('Enter name of candidate :')
                c = int(input('Enter age in numbers :'))
                d = input('Enter gender (M or F) :')
                e = input('Enter exam_centre :')
                f = input('Enter school name :')
                g = input('Enter city :')
                h = float(input("Enter maths score :"))
                i = float(input('Enter science number :'))
                j = float(input("Enter sst score :"))
                k = float(input("Enter english score :"))
                l = float(input("Enter hindi number :"))
                m = float(input("Enter total score :"))
                n = float(input("Enter percentage obtained :"))
                o = input("Enter passing_status of candidate :")
                data={"rno":a,"name":b,"age":c,"gender":d,"exam_centre":e,"school":f,"city":g,"maths":h,"science":i,"sst":j,"english":k,"hindi":l,"total":m,"percentage":n,"passing_status":o}
                df = df.append(data,ignore_index=True)
                print(df.tail(5))
                print('\n\n\n Press any key to continue....')
                wait = input()
            if ch == 4:
                print("\n",df.columns,"\n")
                col_name = input('Enter Column Name that You want to print : ')
                print(df[col_name])
                print('\n\n\n Press any key to continue....')
                wait = input()                               
            if ch == 5:
                i=int(input('Enter Roll Number of student whose data needs to be display : '))
                print("\n Following is the data of the Roll Number - ",i,"\n")
                print(df.loc[df.rno==i])
                print('\n\n\n Press any key to continue....')
                wait = input()              
            if ch==6:
                col=int(input("Enter number of records which you want to display from Top or Bottom : "))
                T=input("Press H to show Top or T for bottom records : ")
                if T == "H":
                        print(df.head(col))
                else:
                        print(df.tail(col))

                print('\n\n\n Press any key to continue....')
                wait=input()           
            if ch==7:
                print(df.columns,"\n")
                col_name=input("Enter the column name which you want to sort :")
                v=bool(input("For ascending write True otherwise only press Enter:"))
                print(df.sort_values(col_name,ascending=v))
                print('\n\n\n Press any key to continue....')
                wait=input()            
            if ch==8:
                print(df.columns,"\n")
                col_name = input('Enter the column name which you want to delete:')
                df=df.drop(col_name,axis=1)
                print(df)
                print('\n\n\n Press any key to continue....')
                wait = input()
            if ch == 9:
                E=int(input("Enter the index which you want to delete from the DataFrame : "))
                df=df.drop(E)
                print(df.loc[E-2:E+2])
                print('\n\n\n Press any key to continue....')
                wait = input()
            if ch == 10:
                break
def graph():
    df = pd.read_csv(csv_file,index_col="rno")
    while True:
        print('\n                                           GRAPH MENU')
        print('*'*100)
        print('1.  Making of Line graphs of a particular student with all subject scores on y-axis\n')
        print('2.  Making of Bar graph for number of students of various schools or exam centre\n')
        print('3.  Displaying the number of male and female candidates appeared in exam\n')
        print('4.  Making of Histogram for number of students within range of their percentage value\n')
        print('5.  Making of Scatter Graph for showing marks of particular student in all subjects \n')
        print('6.  Exit (Exit From Graph Menu)\n')
        ch = int(input('Enter your choice:'))

        if ch == 1:
            a=int(input("Enter roll number of which you want a line graph of different subject's marks : "))
            b=df.loc[a,"maths"]
            c=df.loc[a,"science"]
            d=df.loc[a,"sst"]
            e=df.loc[a,"english"]
            f=df.loc[a,"hindi"]
            x=("Maths","Science","Sst","English","Hindi")
            y=(b,c,d,e,f)
            plt.plot(x,y,color="b",linewidth=2,marker="*",markersize=10,markeredgecolor="k")
            plt.xlabel("Subjects")
            plt.ylabel("Marks distrubution")
            plt.title("Line graph of marks of a particular student")
            plt.grid(True)
            plt.show()
        if ch == 2:
            i=input("Press S for school distribution or Press E for Exam Centre distribution of total students :")
            if i == "S":
                    x =("MGD","JVP","Rawat","Oxford")
                    g =df.groupby('school')
                    y =g['school'].count()
                    plt.xlabel('School')
                    plt.ylabel('Total Students')
                    plt.title('School wise children count')
                    plt.bar(x,y,color=["red","b","black","g"],width=0.5)
                    plt.yticks(y)
                    plt.grid(True)
                    plt.show()
            else:
                    z=("SR Global","Subodh","Sunshine")
                    f=df.groupby("exam_centre")
                    y=f["exam_centre"].count()
                    plt.xlabel("Exam Centres")
                    plt.ylabel("Number of students")
                    plt.title("Exam Centre wise distribution")
                    plt.bar(z,y,color="m",width=0.5)
                    plt.yticks(y)
                    plt.grid(True)
                    plt.show()
                   
        if ch ==3:
            f=df.groupby("gender")
            x=df["gender"].unique()
            y=f["gender"].count()
            plt.xlabel("Gender")
            plt.ylabel("Number of students")
            plt.title("Gender Wise number of  Candidates")
            plt.bar(x,y,color="r",width=0.25)
            plt.grid(True)
            plt.show()
        if ch==4:
                x=df["percentage"]
                plt.hist(x,bins=10,color="y")
                plt.xlabel("Range of percentage")
                plt.ylabel("Number of students")
                plt.grid(True)
                plt.title("Number of students within range of their percentage value")
                plt.show()
        if ch==5:
                a=int(input("Enter roll number of which you want a line graph of different subject's marks : "))
                b=df.loc[a,"maths"]
                c=df.loc[a,"science"]
                d=df.loc[a,"sst"]
                e=df.loc[a,"english"]
                f=df.loc[a,"hindi"]

                x=("Maths","Science","Sst","English","Hindi")
                y=(b,c,d,e,f)
                plt.plot(x,y,"o",markersize=5,markeredgecolor="r")
                plt.title("Showing marks of particular student in all subjects")
                plt.grid(True)
                plt.xlabel("Subjects")
                plt.ylabel("Marks distribution")
                plt.show()
       
        
        if ch == 6:
            break
        
result_data_analysis()

graph()

print("Thanks For Visiting")
