import tkinter as tk
from tkinter import *
import re
import requests
import codecs
from lxml import html
import os
import sys
import urllib
import copy
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import glob
import pandas as pd
import csv
import shutil
path = "../chromedriver"
def certif():
    def get_certif():
        global username_s
        username_s = u2.get("1.0", "end-1c")
        global password_s
        password_s = p2.get("1.0", "end-1c")
        root.destroy()

    root = Tk()
    root.title('Function')
    root.geometry("900x300")
    u1 = Label(root, text="Enter username: ")#.grid(row=1, column= 0,sticky=W) 
    u1.grid(row=0, column= 1,sticky=W) 

    u2 = Text(root,height = 1,width = 25)
    u2.grid(row=0, column= 2,sticky=W) 

    p1 = Label(root, text="Enter password: ")#.grid(row=1, column= 0,sticky=W) 
    p1.grid(row=1, column= 1,sticky=W) 

    p2 = Text(root,height = 1,width = 25)
    p2.grid(row=1, column= 2,sticky=W) 

    f3 = tk.Button(root, text="Enter", command=get_certif)#.grid(row=1, column=2, sticky=W)
    #f3 = tk.Button(root, text="Enter").grid(row=1, column=2, sticky=W)
    # f3.pack()
    f3.grid(row=1, column= 3,sticky=W) 

    root.mainloop()
certif()
#repeated run until username and password is not null !!!
while not (username_s != '' and password_s != '' ): 
    username_s = ''
    password_s = ''
    certif()



def main():
    global root 
    root = Tk()
    root.title('Function')
    root.geometry("900x300")
    # frmLT = Frame(width=500, height=320, bg='white')
    # frmLT.grid(row=0, column=0,padx=1,pady=3)

    mystring = StringVar()
    first_function = Button(root, text="Scan URL and create download list", command=first_print).grid(row=0, column=0, sticky=W)
    # second_function = Button(root, text="Download and extract feature", command=second_f).grid(row=0, column=1, sticky=W)
    # third_function = Button(root, text="Combine and get unique item", command=third_f).grid(row=0, column=2, sticky=W)

    root.mainloop()


def append_multiple_lines(file_name, lines_to_append, mode):
    # Open the file in append & read mode ('a+')
    with open(file_name, mode) as file_object:
        appendEOL = False
        # Move read cursor to the start of file.
        file_object.seek(0)
        # Check if file is not empty
        if mode == "a+":
            data = file_object.read(100)
            if len(data) > 0:
                appendEOL = True
        # Iterate over each string in the list
        for line in lines_to_append:
            # If file is not empty then append '\n' before first line for
            # other lines always append '\n' before appending line
            if appendEOL == True:
                file_object.write("\n")
            else:
                appendEOL = True
            # Append element at the end of file
            file_object.write(line)


def first_print():
    result_text = tk.StringVar()
    list_value = tk.StringVar()
    list_value.set(("Computer & tablets", "Consumber electronics","hardware","Apparel","Cookware","Domestics","Food & Sundries",
    "Footwear","Garden/Patio","Health & beauty","Home Comfort","Home furnishings","Luggage","Major appliances","Mixed Lots",
    "Printers","Rugs","Seasonal","Small appliances","Sporting goods","Vacuums"))

    url_list = ["https://bstock.com/costco/all-inventory/computers-tablets/?limit=48",
            "https://bstock.com/costco/all-inventory/small-electronics/?limit=48",
            "https://bstock.com/costco/all-inventory/hardware/?limit=48",
            "https://bstock.com/costco/all-inventory/apparel/?limit=48",
            "https://bstock.com/costco/all-inventory/cookware/?limit=48",
            "https://bstock.com/costco/all-inventory/domestics/?limit=48",
            "https://bstock.com/costco/all-inventory/sundries/?limit=48",
            "https://bstock.com/costco/all-inventory/footwear/?limit=48",
            "https://bstock.com/costco/all-inventory/garden-patio/?limit=48",
            "https://bstock.com/costco/all-inventory/health-beauty/?limit=48",
            "https://bstock.com/costco/all-inventory/home-comfort/?limit=48",
            "https://bstock.com/costco/all-inventory/home-furnishings/?limit=48",
            "https://bstock.com/costco/all-inventory/luggage/?limit=48",
            "https://bstock.com/costco/all-inventory/major-appliances/?limit=48",
            "https://bstock.com/costco/all-inventory/mixed-lots/?limit=48",
            "https://bstock.com/costco/all-inventory/printers/?limit=48",
            "https://bstock.com/costco/all-inventory/rugs/?limit=48",
            "https://bstock.com/costco/all-inventory/seasonal/?limit=48",
            "https://bstock.com/costco/all-inventory/small-appliances/?limit=48",
            "https://bstock.com/costco/all-inventory/toys-sporting-goods/?limit=48",
            "https://bstock.com/costco/all-inventory/vacuums/?limit=48"]
    
    
    def start_working():
        if len(f2.curselection()) == 0:
            url = k2.get("1.0", "end-1c")
            dir_file_name = 'url_entered'
            
        # var1.set(f2.get(f2.curselection()))
        # print(len(f2.curselection()))
        # input("check!!!")
        
        else:
            choose_url_index = f2.curselection()[0]
            url = url_list[choose_url_index]
            dir_file_name = f2.get(f2.curselection())
        
        if not os.path.exists(dir_file_name):
            os.makedirs(dir_file_name)

        os.chdir('./'+dir_file_name)

        # url = "https://bstock.com/costco/all-inventory/computers-tablets/?p=2"

        # print(url)
        # input("check !!!!")
        # print(url)
        # print(dir_file_name)
        # f2.destroy()
        # result_text.set(url)
        # print(result_text.get())
        # print(type(f2.curselection()))
        
        driver = webdriver.Chrome(path)
        driver.get(url)
        sleep(1)

        username = driver.find_element_by_id("loginId")
        username.clear()
        # username.send_keys("Info@techfrys.com")
        username.send_keys(username_s)

        password = driver.find_element_by_id("password")
        password.clear()
        # password.send_keys("T8QvUJ6zn5!gcpP")
        password.send_keys(password_s)
        driver.find_element_by_tag_name("button").click()

        sleep(2)
        text = driver.page_source
        
        wrong_pass_re = re.compile(r'Invalid login credentials')
        wrong_pass = wrong_pass_re.findall(text)
        if len(wrong_pass) != 0 : 
            root.destroy()
            driver.quit()
            print("Wrong username or password")
            exit()
        regex_product = re.compile(r'<li id=.*?</li>',re.DOTALL)

        information = regex_product.findall(text)
        # print(len(information))

        # print(information[0])
        information_str = ''.join(information)

        regex_product_url_regex = re.compile(r'https://bstock.com/costco/auction/auction/view/id.\d{6}')
        result_product_url_list = regex_product_url_regex.findall(information_str)

        #check all the url list
        # def get_information(url_list):
        #     for url in url_list:
        #         print(url)
        #     print()

        result_product_url_list = list(dict.fromkeys(result_product_url_list))

        # get_information(result_product_url_list)
        # input("check?")

        # fileToRead.close()
        driver.quit()

        append_multiple_lines("scan_url.txt",result_product_url_list,"a+")
        
        # print("\nFinish Scan. All data store in file : 'scan_url.txt' \n")
        # result_text.set("Finish Scan.\n All data store in file : 'scan_url.txt'")
        # f1.destroy()
        # f2.destroy()
        # f3.destroy()
        # k1.destroy()
        # k2.destroy()

        result_text = tk.StringVar()
        # result = tk.Label(root, textvariable=result_text)#.grid(row=2, column= 0,sticky=W)
        # #result.pack()
        # result.grid(row=4, columnspan = 4,sticky=W)
        f = open("scan_url.txt")
        readline= f.readlines()
        information_str = ''.join(readline)
        if len(information_str) == 0:
            print("Please start with first function !")
            return

        if not os.path.exists('download_csv'):
            os.makedirs('download_csv')
        if not os.path.exists('result'):
            os.makedirs('result')
        # print(" Download! \n ")
        
        regex_product_url_regex = re.compile(r'https://bstock.com/costco/auction/auction/view/id.\d{6}')
        result_product_url_list = regex_product_url_regex.findall(information_str)
        # temp is to write back to the txt file
        temp = copy.copy(result_product_url_list)

        header = ("Six code","Current bid","Minimum bid Interval","Shipment cost","Bid close time","Costco code","Webpage url","Ext. Retail","Condition")
        
        if not os.path.exists("./result/information-%s.csv"%(dir_file_name)):
            with  open('./result/information-%s.csv'%(dir_file_name), 'w', newline='') as outputcsv:
                writer = csv.writer(outputcsv)
                writer.writerow(header)
        for page_url in result_product_url_list:
        # for i in range(0,len(result_product_url_list)):
        #     page_url = result_product_url_list[i]

            # counter +=1
            # print("counter: "+str(counter) )
            # counter -=1
            # if counter == 0:
            #     input("\nPress any key to Contiune!\n")
            #     counter =5
            # input("continue_loop?")
            # html = requests.get(page_url)
            # text = html.text
            #----------------------------------------open page one by one
            driver = webdriver.Chrome(path)
            # driver.maximize_window()
            driver.get(page_url)

            username = driver.find_element_by_id("loginId")
            username.clear()
            # username.send_keys("Info@techfrys.com")
            username.send_keys(username_s)

            password = driver.find_element_by_id("password")
            password.clear()
            # password.send_keys("T8QvUJ6zn5!gcpP")
            password.send_keys(password_s)

            driver.find_element_by_tag_name("button").click()

            sleep(3)
            
            print("Start crawling down information")

            text = driver.page_source
            wrong_pass_re = re.compile(r'Invalid login credentials')
            wrong_pass = wrong_pass_re.findall(text)
            if len(wrong_pass) != 0 : 
                root.destroy()
                driver.quit()
                print("Wrong username or password")
                exit()
            # fileToWrite = open("temp2.html", "w")
            # fileToWrite.write(pageSource)
            # fileToWrite.close()
            # fileToRead = open("temp2.html", "r")
            # text = fileToRead.read()
            auction_ended_regex = re.compile(r'Auction ended')
            auction_ended = auction_ended_regex.findall(text)
            # print(auction_ended)
            # print(len(auction_ended))
            # input("correct?")
            if len(auction_ended) != 0:
                #fileToRead.close()
                driver.quit()
                temp.pop(0)
                append_multiple_lines("scan_url.txt",temp,"w")
                # print(str(page_url) + "\nHave finish the auction. Skip it from the download\n")
                # print("\nUpdated scan_file.txt file ! \n")
                # show_text = str(page_url) + "\nHave finish the auction. Skip it from the download\n"+"Updated scan_file.txt file ! \n"
                # result = tk.Label(root, textvariable=result_text)#.grid(row=2, column= 0,sticky=W)
                # #result.pack()
                # result.grid(row=4, columnspan = 4,sticky=W)
                # result_text.set(show_text)
                # result.update()

                if len(temp)==0:
                    # show_text = show_text+"Finish all the file.\n"
                    # result_text.set(show_text)
                    break
                continue
            # input("checkpoint2")
            print("File is valid! ")
            # --------------find 6 code
            d_6_regex = re.compile(r'\d{6}?')
            d_6 = d_6_regex.findall(page_url)
            d_6 = str(d_6[0]. replace(',', ''))
            # print(d_6)

            # -------------- find current bid
            cur_bid_regex = re.compile(r'<span id="current_bid_amount">.*?</span>',re.DOTALL) 
            cur_bid = cur_bid_regex.findall(text)
            # print(cur_bid)

            cur_bid_str = ''.join(cur_bid)
            #remove newline
            # cur_bid_str = cur_bid_str.strip()
            # print(cur_bid_str)
            cur_bid_regex2 = re.compile(r'\d+,*\d*',re.DOTALL)
            cur_bid = cur_bid_regex2.findall(cur_bid_str)
            # print(cur_bid)
            #conver from list to a int
            cur_bid = float(cur_bid[0]. replace(',', ''))

            #----------------------------------find the minimum bid

            next_bid_regex = re.compile(r'<span id="next_current_bid".*?</span>',re.DOTALL) 
            next_bid = next_bid_regex.findall(text)
            # print(next_bid)

            next_bid_str = ''.join(next_bid)
            next_bid_regex2 = re.compile(r'\d+,*\d*',re.DOTALL)
            next_bid = next_bid_regex2.findall(next_bid_str)
            # print(next_bid)

            next_bid = float(next_bid[0].replace(',', ''))
            # print(next_bid)
            minimum_price = next_bid - cur_bid

            #--------------------------------shipment cost
            shipment_regex = re.compile(r'<span id="shipping_cost".*?</span>',re.DOTALL)
            shipment_cost = shipment_regex.findall(text)
            shipment_cost_str = ''.join(shipment_cost)
            shipment_regex2= re.compile(r'\d+,*\d*.?\d{2}?',re.DOTALL)
            shipment_cost = shipment_regex2.findall(shipment_cost_str)
            if len(shipment_cost) == 0:
                shipment_cost =0
            else:
                shipment_cost = float(shipment_cost[0].replace(',',''))
            # print(shipment_cost)


            #------------------------------- close date 
            end_time_regex = re.compile(r'<span id="auction_end_time".*?</span>',re.DOTALL)
            end_time = end_time_regex.findall(text)
            end_time_str = ''.join(end_time)
            end_time_regex2= re.compile(r'\S{3} \S+ \d+,.* PM|AM',re.DOTALL)
            end_time = end_time_regex2.findall(end_time_str)
            # print(end_time)
            end_time = end_time[0].replace(',','')
            # print(end_time)

            #-----------------short name #MON-2734918
            title_regex = re.compile(r'<h1 itemprop="name".*?</h1>',re.DOTALL)
            title = title_regex.findall(text)
            title_str = ''.join(title)
            # print(title_str)


            title_regex2= re.compile(r'\S{3}\-\d+',re.DOTALL)
            title = title_regex2.findall(title_str)
            # print(title)
            title = title[0].replace(',','')
            # print(title)

            #-----------get condition
            condition_regex = re.compile(r'data cleared|new condition|like new|A/B|Mixed Condition|C/D',re.IGNORECASE)
            condition_find = condition_regex.findall(title_str)
            if len(condition_find) ==0:
                condition_string = "Not specificed"
            # print(cur_bid)
            # condition_string = ''.join(condition_find)
            else:
                condition_string = condition_find[0].replace(',','')


            #---------get download URL 
            d_url_regex = re.compile(r'<button class="button" onclick.*?</button>')
            d_url = d_url_regex.findall(text)
            d_url_str = ''.join(d_url)
            # print(d_url_str)
            d_url_regex2= re.compile(r'https.*csv')
            d_url = d_url_regex2.findall(d_url_str)
            # print(d_url)
            d_url = d_url[0].replace(',','')
            # print(d_url)

            #--------------------get condition !!


            # title_regex = re.compile(r'<h1 itemprop="name.*?</h1>',re.DOTALL) 
            # title_find = title_regex.findall(text)
            # title_str = ''.join(title_find)
            # # print(cur_bid_str)

            # condition_regex = re.compile(r'data cleared|new condition|like new',re.IGNORECASE)
            # condition_find = condition_regex.findall(title_str)
            # # print(cur_bid)
            # condition_string = ''.join(condition_find)



            urllib.request.urlretrieve(d_url, './download_csv/%s.csv'%(title))
            file_name = title + ".csv"

            df = pd.read_csv("./download_csv/%s"%(file_name))
            df["Costco Order#"] = title
            ext_retail_total = df['Ext. Retail'].sum()

            # remove Inmar order # due the combine problem.
            a = list(df.columns)
            if('Inmar Order #' in a):
                a.remove('Inmar Order #')

            # df["Inmar Order#"] = d_6
            df[a].to_csv("./download_csv/%s"%(file_name), index=False)

            # input("maker sure xxx-xx.csv in download_csv dirctory the file added information current!!!")

            # print(d_6)
            # print(cur_bid)
            # print(minimum_price)
            # print(shipment_cost)
            # print(end_time)
            # print(title)
            # print(page_url)
            
            scan_infor = (str(d_6),str(cur_bid),float(minimum_price),float(shipment_cost),str(end_time),str(title),str(page_url),float(ext_retail_total),str(condition_string))
            with  open('./result/information-%s.csv'%(dir_file_name), 'a+', newline='') as outputcsv:
                writer = csv.writer(outputcsv)
                writer.writerow(scan_infor)
            print("\nUpdate the scanned informtaion to result/information-%s.csv"%(dir_file_name))

            # input("make sure information.csv is correct")
            # list_d6 = ["Six code is : ", d_6]
            # list_cur_bid= ["Current bid is : ", cur_bid]
            # list_minimum_price = ["Minimum bid price is : ", minimum_price]
            # list_shipment_cost = ["shipment cost is : ", shipment_cost]
            # list_endtime = ["Bid end time is  : " , end_time]
            # list_title = ["The name is : ", title]
            # from csv import writer
            # def append_list_as_row(file_name, list_of_elem):
            #     # Open file in append mode
            #     with open(file_name, 'a+', newline='') as write_obj:
            #         # Create a writer object from csv module
            #         csv_writer = writer(write_obj)
            #         # Add contents of list as last row in the csv file
            #         csv_writer.writerow(list_of_elem)

            # row_contents = [32,'Shaun','Java','Tokyo','Morning']
            # Append a list as new line to an old csv file

            # append_list_as_row(file_name, list_d6)
            # append_list_as_row(file_name, list_cur_bid)
            # append_list_as_row(file_name, list_minimum_price)
            # append_list_as_row(file_name, list_shipment_cost)
            # append_list_as_row(file_name, list_endtime)
            # append_list_as_row(file_name, list_title)

            driver.quit()
            temp.pop(0)
            append_multiple_lines("scan_url.txt",temp,"w")
            # fileToRead.close()

            # sleep(2)
            # print("Finish file:  " + title + ".csv ! Store at download_csv dirctory \n")
            # print("Updated scan_file.txt file ! \n")
            
            # show_text = "Finish file:  " + title + ".csv ! Store at download_csv dirctory \n" + "Updated scan_file.txt file ! \n"
            # result = tk.Label(root, textvariable=result_text)#.grid(row=2, column= 0,sticky=W)
            #     #result.pack()
            # result.grid(row=4, columnspan = 4,sticky=W)
            # result_text.set(show_text)
            # result.update()

            # print(str(len(temp))+"!!!!")
            # input("check")
            if len(temp)==0:
                # show_text = show_text+"Finish all the file.\n"
                # result_text.set(show_text)
                break
        

        result_text = tk.StringVar()

        if not os.path.exists('download_csv'):
            return
        if not os.path.exists('result'):
            os.makedirs('result')
        os.chdir('./download_csv')
        extension = 'csv'
        all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
        combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
        os.chdir('../result')
        # combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
        combined_csv.to_csv( "combined_csv-%s.csv"%(dir_file_name), index=False)
        # print("\nCombine all the csv file store at result/combined_csv.csv\n")

        #extract two features from the csv file
        with open('combined_csv-%s.csv'%(dir_file_name), newline='') as inputcsv, open('temp.csv', 'w', newline='') as outputcsv:
            fieldnames = ('Costco Item #', 'Item Description')
            
            # writer = csv.DictWriter(outputcsv, fieldnames=fieldnames)
            # writer = csv.DictWriter(outputcsv,fieldnames=fieldnames)
            data = csv.DictReader(inputcsv)
            # print("Costco Item #")
            writer = csv.writer(outputcsv)
            writer.writerow(fieldnames)
            # data = csv.reader(inputcsv)

            #print("---------------------------------")
            for row in data:
                # print(row['\ufeffCostco Item #'], row['Item Description'])
                # print(row)
                dataselect = row[next(iter(row))], row['Item Description']
                writer.writerow(dataselect)
                # print(dataselect)
                # print(row[next(iter(row))])

        #remove duplicates of the two features.
        with open('temp.csv','r') as in_file, open('unique_item-%s.csv'%(dir_file_name),'w') as out_file:
            seen = set() # set for fast O(1) amortized lookup
            for line in in_file:
                if line in seen: continue # skip duplicate
                seen.add(line)
                out_file.write(line)
        os.remove("./temp.csv")
        os.chdir('..')
        # shutil.rmtree("./download_csv")

        os.chdir('..')
        # print("\nDelete download_csv dirctory\n")
        # print("\nFinish combine file, stored all unique items at result/unique_item.csv! \n")

        show_text = "Stored all information in ./information-%s.csv\n"%(dir_file_name) +  \
            "Combine all the csv file store at result/combined_csv-%s.csv\n"%(dir_file_name) + \
                    "Stored all unique items at result/unique_item-%s.csv! "%(dir_file_name) 
        result = tk.Label(root, textvariable=result_text)#.grid(row=2, column= 0,sticky=W)
            #result.pack()
        result.grid(row=4, columnspan = 4,sticky=W)
        result_text.set(show_text)
        result.update()
                  


    f1 = Label(root, text="Choose a catagry to contiune")#.grid(row=1, column= 0,sticky=W) 
    #f1.pack()
    f1.grid(row=1, column= 0,sticky=W) 

    f2 = tk.Listbox(root, listvariable=list_value)#.grid(row=1,column= 1,sticky=W)
    # f2.pack()
    f2.grid(row=1, column= 1,sticky=W) 

    f3 = tk.Button(root, text="Enter", command=start_working)#.grid(row=1, column=2, sticky=W)
    #f3 = tk.Button(root, text="Enter").grid(row=1, column=2, sticky=W)
    # f3.pack()
    f3.grid(row=1, column= 2,sticky=W) 
    result_text.set("")
    result = tk.Label(root, textvariable=result_text)#.grid(row=2, column= 0,sticky=W)
    #result.pack()
    result.grid(row=4, columnspan = 4,sticky=W)
    result.update()

    k1 = Label(root, text="Or Enter URL")#.grid(row=1, column= 0,sticky=W) 
    k1.grid(row=2, column= 0,sticky=W) 

    k2 = Text(root,height = 1,width = 25)
    k2.grid(row=2, column= 1,sticky=W) 


main()