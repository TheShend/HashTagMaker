import pyperclip
import pyautogui as pag
import time

def ready_for_hash(lht):
  for l in list("""\';"][}{!@#$%^&*()_+~=-؟|؛،:<>}],./"""):
    lht=lht.replace(l,"")
  time.sleep(0.5)
  return(lht)

def excespace_remover(ht):
  fht=""
  lht=ht.splitlines()
  print(lht)
  for s in lht:
    s=s.replace(" ","_")
    s=s.strip("\n")
    htt=""
    for i,l in enumerate(s):
      if (i)>=-1 and (s[i-1]=="_") and l=="_":
        continue
      else:
        htt+=l
    if htt=="":
      fht+="\n"+ htt.strip("_")
    else:
      fht+="\n"+"#"+ htt.strip("_")
  return(fht)

pag.hotkey('alt','tab')
time.sleep(0.5)
pag.hotkey('ctrl','a')
time.sleep(0.5)
pag.hotkey('ctrl','c')
time.sleep(0.5)
# pag.hotkey('alt','tab')

ht=excespace_remover( ready_for_hash(pyperclip.paste()))

pyperclip.copy(ht)
# time.sleep(0.5)
# pag.hotkey('alt','tab')
time.sleep(0.5)
pag.hotkey('ctrl','v')
