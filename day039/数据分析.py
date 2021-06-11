# Excel数据的可视化分析
import openpyxl
import matplotlib.pyplot as plt

Shoe_Sales_Data = openpyxl.load_workbook("data/20210610.xlsx")
sheet = Shoe_Sales_Data['Sheet1']
colors = []
sizes = []

for i in range(1, 21):
    colors.append(sheet['A' + str(i)].value)
    sizes.append(sheet['B' + str(i)].value)

count = len(colors)
color_class = set(colors)
color_percent = []
for clr in color_class:
    color_percent.append(colors.count(clr) / count)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.pie(x=color_percent, labels=color_class, autopct='%1.3f%%')
plt.legend()
plt.savefig("data/20210610.png")
