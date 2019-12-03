import pandas as pd
x = {'Box':['Box 1','Box 1','Box 1','Box 2','Box 2','Box 2'],'Dimention':['Length','Width','Height','Length','Width','Height'],'Value':[6,4,2,5,3,4]}
messy = pd.DataFrame(x,columns=['Box','Dimention','Value'])
tidy = messy.pivot_table(index='Box',columns='Dimention',values='Value')
final_tidy = tidy.assign(Volume = tidy.Length*tidy.Width*tidy.Height)
print (final_tidy)