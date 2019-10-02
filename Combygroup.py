import vk
import codecs
import encodings
#APP_ID = 5908236             #ID приложения!!!
import re
import webbrowser
from random import randint as rand
from time import sleep

nignor=['vk.com/photo','vk.com/video']
ignor=['vk.com/doc','vk.com/audio','vk.cc/4ut1ah','vk.cc/5VKrFT','vk.cc/4OTuOH','vk.cc/3HCSFe','stach.bk.ru','vk.cc/5gz9Ea','vk.cc/4V8c3R','KA4KA00','vk.cc/4SKDIK','vk.cc/3GXFiT','vk.cc/3VaFgj','vk.cc/4cs94d','vk.cc/4W4T3u','vk.cc/4o7Reu','vk.cc/5bMWhw','vk.com/big_tanks','vk.cc/5aFMfv','vk.cc/57Aeeu','vk.cc/5bHb5q','137972127','55088406','vk.cc/5c5Hqg','vk.cc/5kOd4Z','vk.cc/4Xfbry','popka.rus']
#idsadm=[-55088406,66601928,30382931,248149071,137621301,160967530,201289140,217876267,71012818,299415116,240210451,140060341,106980822,150503319,225586643,115220271,158435442,281229133,149040817,58672307,187321074,173596394,377384379,181469961,279097696]  # id-шники админов
doms=['.ru/','.com/','.net/','.it/','.xyz/','.bid/','.sk/','.tv/','.org/','.ly/','.pp/','.be/','.su/','.tk/','.me/','.cc/','.gl/']
#anslinks=['Размещение рекламных/посторонних ссылок в комментариях запрещено правилами группы -> vk.cc/4W4T3u','Реклама/рекламные ссылки/видео в комментариях запрещены. Читайте правила группы и не нарушайте их, пожалуйста! См. Правила группы: vk.cc/4W4T3u']
#anscaps=['Не пишите заглавными буквами, пожалуйста. Caps Lock запрещен правилами группы -> vk.cc/4W4T3u','Выключите Caps Lock (клавиша между Tab и Shift)','Выключите Caps Lock (Кнопка между Shift и Tab), пожалуйста. Писать большими буквами запрещено! См. Правила группы: vk.cc/4W4T3u']

fi=open('idsadm.txt','r')
idsadm=[int(i) for i in fi]
fi.close()

twerk=-55088406  # id страницы
print('Вас приветствует программа по сбору комментов.')
print('Ссылки на некоторые нарушения будут приходить вам в ЛС')
print('Со всеми возникшими вопросами обращатсья по адресу vk.com/di2048')
#how=15 # сколько постов анализировать
print('Введите кол-во анализируемых постов. От этого зависит скорость работы. Я обычно ввожу 8 в период большой активности.')
how=int(input())
print("Введите номера тех постов, с которых читать комменты не нужно. Например:")
print('2484448 2484383 2484334     И ENTER после ввода или пустой строки для начала работы')
print('Я это исключаю НЧ и КБЛ, так как слежу за ними сам более внимательно, чем за всем остальным')
postes=list(map(int,input().split()))
#linksuda=103959481  # куда кидать ссыль на удаляемое (2000000000 + id беседы./id пользователя.)

# приобретаем токен
def gettoken():
        import webbrowser
        APP_ID = 5908236             #ID приложения!!!
        def get_auth_params():
            auth_url = ("https://oauth.vk.com/authorize?client_id={app_id}"
                        "&scope=69632&redirect_uri=http://oauth.vk.com/blank.html"  #тут легче использовать число
                        "&display=page&response_type=token".format(app_id=APP_ID))
            webbrowser.open_new_tab(auth_url)
            redirected_url = input("Paste here url you were redirected(адрес из строки браузера сюда вставь):\n")
            q=redirected_url.index('token')
            return redirected_url[q+6:q+91]
        return get_auth_params()
        #https://vk.com/dev/permissions

try:
        fi=open('token.txt','r')
except:
        token=gettoken()
        fi.close()
        fi=open('token.txt','w')
        fi.write(token)
        fi.close()
fi=open('token.txt','r')
s=fi.read()
fi.close()

#s='фыв516f77bed8324e4f464c760a2e364c9f5cedd9dd8f823c6fd88e60dbf5827e7ed0fa09df54c95ea426c16'
session = vk.Session(access_token=s)
api = vk.API(session)

# куда кидать ссыль

linksuda=api.users.get(v=5.62)[0]['id']

sleep(1)
def sendlink(po,nu,dop):
        mes='https://vk.com/big_tanks?w=wall-55088406_'+str(po)+'_r'+str(nu)+' '+dop
        qwer=api.messages.send(message=mes,random_id=int(str(po)+str(nu)),peer_id=linksuda,v=5.62)
print("LET'S GO)")
def main():
    def getpo(o):
        return api.wall.get(owner_id=twerk,offset=o,count=1)[1]['id']

    manid={}
    for i in range(0,how):
        tyr=getpo(i)
        sleep(0.4) #0.06
        ti=api.wall.getComments(owner_id=twerk,post_id=tyr,count=1,sort='desc')
        if ti[0]==0:
            manid[tyr]=0
        else:
            manid[tyr]=ti[1]['cid']
        sleep(0.5)
        
    def getlinks(chat_string):
        pattern = '(?:https?:\/\/)?(?:[\w\.]+)\.(?:[a-z]{2,6}\.?)(?:\/[\w\.]*)*\/?'
        chat_string=chat_string.lower()
        tes={chr(i) for i in range(ord('а'),ord('я')+1)}
        q=re.findall(pattern, chat_string)
        q=[i+'/' for i in q]
        for i in range(len(q)-1,-1,-1):
            bole=True
            for jd in doms:
                if jd in q[i]:
                    bole=False
            if (len(set(q[i][:q[i].find('.')])&tes)!=0)|(bole):
                q.pop(i)
        return q

    def haslink(s):
        if len(getlinks(s))==0:
            return False
        else:
            return True
                    
    def comanliz(norm,idp,adb=True):
        sti=norm['text']+' '
        try:
                print('### '+sti)
        except:
                print('### ###смайл###')
        print() # ска
        if sti[0:3]=='[id':
            sti=sti[sti.index(' '):]
        le=sti.count(' ')
        #print(sti,le)
        if 'vk.com/photo' in sti:
                '''
            ids=str(norm['from_id'])
            naem=api.users.get(user_ids=ids)[0]['first_name']
            # тут ФОТО
            #qwer=api.wall.createComment(owner_id=twerk,post_id=idp,reply_to_comment=norm['cid'],message='[id'+str(norm["uid"])+'|'+naem+'], Пожалуйста, свои скриншоты/картинки/фотографии публикуйте в фотоальбом: http://vk.cc/5gz9Ea',guid=str(norm['date'])+naem)
            sendlink(idp,norm['cid'],'фото')
            print(norm['text'])
            print()'''
        elif 'vk.com/video' in sti:
            ids=str(norm['from_id'])
            naem=api.users.get(user_ids=ids)[0]['first_name']
            # тут ВИДЕО
            #qwer=api.wall.createComment(owner_id=twerk,post_id=idp,reply_to_comment=norm['cid'],message='[id'+str(norm["uid"])+'|'+naem+'], Видео в комментариях запрещены правилами группы -> vk.cc/4W4T3u',guid=str(norm['date'])+naem)
            if adb:
                    sendlink(idp,norm['cid'],'видео')
                    try:
                            print(norm['text'])
                    except:
                            print(1234567890)
            print()
        elif (sti.isupper()|(len(re.findall('[a-z,а-я]',sti))*8<len(re.findall('[A-Z,А-Я]',sti))))&(le>1):
            ids=str(norm['from_id'])
            naem=api.users.get(user_ids=ids)[0]['first_name']
            # тут про КАПС
            #indexx=rand(0,len(anscaps)-1)
            #qwer=api.wall.createComment(owner_id=twerk,post_id=idp,reply_to_comment=norm['cid'],message='[id'+str(norm["uid"])+'|'+naem+'], '+anscaps[indexx],guid=str(norm['date'])+naem)
            if adb:
                    sendlink(idp,norm['cid'],'капс')
                    try:
                            print(norm['text'])
                    except:
                            print(1234567890)
            print()
        else:
            if 'tankionline.com/battle-ru.html' in sti:
                ids=str(norm['from_id'])
                naem=api.users.get(user_ids=ids)[0]['first_name']
                # тут БОИ
                #qwer=api.wall.createComment(owner_id=twerk,post_id=idp,reply_to_comment=norm['cid'],message='[id'+str(norm["uid"])+'|'+naem+'], Для ссылок на битвы существует игровой чат.',guid=str(norm['date'])+naem)
                if adb:
                        sendlink(idp,norm['cid'],'бой')
                        try:
                            print(norm['text'])
                        except:
                            print(1234567890)
                print()
            elif haslink(sti):
                ids=str(norm['from_id'])
                naem=api.users.get(user_ids=ids)[0]['first_name']
                # тут ССЫЛКИ
                #indexxx=rand(0,len(anslinks)-1)
                #qwer=api.wall.createComment(owner_id=twerk,post_id=idp,reply_to_comment=norm['cid'],message='[id'+str(norm["uid"])+'|'+naem+'], '+anslinks[indexxx],guid=str(norm['date'])+naem)
                # вот тут ты добавил уникальный идентификатор в виде текста самого сообщения, дабы дважды не ругаться на одно и то же
                if adb:
                        sendlink(idp,norm['cid'],'ccылка')
                        try:
                            print(norm['text'])
                        except:
                            print(1234567890)
                print()

    def getcom(idp):
        sleep(0.4)  #0.05
        sid=api.wall.getComments(owner_id=twerk,post_id=idp,sort='desc',count=1)
        if sid[0]==0:
            return None
        else:
            sid=sid[1]['cid']
        cont = sid-manid[idp]
        sleep(0.3) #0.2
        #print(sid,cont)
        if cont>0:
            tex=api.wall.getComments(owner_id=twerk,post_id=idp,sort='desc',count=100)
            for i in tex[1:len(tex)]:
                #print(1)
                if i["cid"]<=manid[idp]:
                    break
                else:
                    Bol=True
                    for inc in ignor:
                        if inc in i['text']:
                            Bol=False
                    for inc in nignor:
                        if inc in i['text']:
                            Bol=True
                    if i['from_id'] in idsadm:
                            print('^^^^^ admin ^^^^^')
                            comanliz(i,idp,False)
                            print('<<<<< admin >>>>>')
                            print()
                    if (i['from_id'] not in idsadm)&(Bol):
                        comanliz(i,idp)
            manid[idp]=sid

    while True:
        # принимаем последние how постов со стены
        # для каждого из них вызываем заполучатель последних комментов
        if getpo(1) not in manid:
            qwe=manid.pop(getpo(how))
            tyr=getpo(1)
            ti=api.wall.getComments(owner_id=twerk,post_id=tyr,count=1,sort='desc')
            if ti[0]==0:
                manid[tyr]=0
            else:
                manid[tyr]=ti[1]['cid']
            sleep(1)
        for i in manid:
            if i not in postes:
                    getcom(i)
                    sleep(0.6)  # меньше надо  #0.4
while True:
    try:
        main()
    except:
        print('ВЫЛЕТ')
        print('ALARM')
        print('')
        print('ALARM')
        print('ПЕРЕПРОВЕРЬТЕ СЛУЧАЙ')  #ПОСЛЕДНИЕ КОМ. НА ВСЯКИЙ 
        sleep(0.5)
        print('GOGOGO!!!')
        print()

'''
main()
'''
'''
проблемы:
СМАЙЛЫ!!
'''
