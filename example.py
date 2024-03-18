import pandas
import random
data = pandas.read_csv("kunuz/kun_uz.csv")
def yangilik():
    rand_son = random.randint(1, 172349)

    title = data["title"][rand_son]
    content = data["content"][rand_son]
    target = data["target"][rand_son]
    
    return f"Yo'nalish: <b>{str(target).capitalize()}</b>\n \nMavzu: <b>{str(title).capitalize()}</b>\n \n<b>{content}</b>"
    
    
# print(yangilik())





