import random
from flask import Flask, request
from pymessenger.bot import Bot
from pymessenger import Element,Button


app = Flask(__name__)
ACCESS_TOKEN = ''
VERIFY_TOKEN = ''
bot = Bot(ACCESS_TOKEN)


#We will receive messages that Facebook sends our bot at this endpoint
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook."""
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
        output = request.get_json()
        print(output)
        for event in output['entry']:
            messaging = event['messaging']
            recipient_id= messaging[0]['sender']['id']
            for message in messaging:
                if message.get('postback'):
                    payload=message.get('postback')['payload']
                    if payload=="news":
                        khoborakhobor(recipient_id)
                    if payload=="sports":
                        kheladhula(recipient_id)

                    if payload=="others":
                        other(recipient_id)

                    if payload=="study":
                        send_study(recipient_id)

                    if payload=="attention":
                        send_attention(recipient_id)

                    if payload=="ipl2020":
                        ipl(recipient_id)
                if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to

                    if message['message'].get('text'):

                        first_msg(recipient_id)


                    if message['message'].get('attachments'):
                        response_sent_nontext = get_message()
                        send_message(recipient_id, response_sent_nontext)
    return "Message Processed"


def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


#chooses a random message to send to the user
def get_message():
    sample_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!", "We're greatful to know you :)"]
    # return selected item to the user
    return random.choice(sample_responses)

#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

def send_generic(recipient_id):
    elements = []
    element1 = Element(title="test", image_url="https://cdn.jpegmini.com/user/images/slider_puffin_before_mobile.jpg", subtitle="subtitle", item_url="http://arsenal.com")
    element2 = Element(title="test2", image_url="https://cdn.jpegmini.com/user/images/slider_puffin_before_mobile.jpg", subtitle="subtitle", item_url="http://arsenal.com")
    elements.append(element1)
    elements.append(element2)
    bot.send_generic_message(recipient_id, elements)

def test_button_message(recipient_id):
    buttons = []
    button = Button(title='Arsenal', type='web_url', url='http://arsenal.com')
    buttons.append(button)
    button = Button(title='Other', type='postback', payload='other')
    buttons.append(button)
    text = 'Select any of them please'
    bot.send_button_message(recipient_id, text, buttons)



def first_msg(recipient_id):
    text=" হ্যালো ব্রাদার, ছোটখাটো এই বটের দুনিয়ায় আমাকে স্বাগতম! তুমি আমাকে রোবট ভাই বলে ডাকতে পারো!!"
    buttons = []
    button1 = Button(title='খবরাখবর', type='postback', payload='news')
    button2 = Button(title='খেলাধুলা', type='postback', payload='sports')
    #button3 = Button(title="ক্ষুধা লাগছে", type='web_url',url='https://www.foodpanda.com.bd/?gclid=Cj0KCQjw2or8BRCNARIsAC_ppyaxlUnuvIHnJUn3cJ026az3ujpRLrEaCq5o1Yv7Zopsc3riG1laJvwaAv9cEALw_wcB')
    button4 = Button(title='অন্যান্য', type='postback', payload='others')
    buttons.append(button1)
    buttons.append(button2)
    #buttons.append(button3)
    buttons.append(button4)
    bot.send_button_message(recipient_id,text,buttons)
    rext = "Shortcuts"
    buttons2=[]
    button3 = Button(title="FOODPANDA", type='web_url', url='https://www.foodpanda.com.bd/')
    button5= Button(title='UBER', type='web_url',url='https://www.uber.com/bd/en/')
    buttons2.append(button3)
    buttons2.append(button5)
    bot.send_button_message(recipient_id,rext,buttons2)
def khoborakhobor(recipient_id):
    elements = []
    elements.append(Element(title="Al Jazeera",image_url='http://logok.org/wp-content/uploads/2014/04/Aljazeera-logo-English-880x660.png',subtitle='Breaking News, World News and Video from Al Jazeera',item_url='https://www.aljazeera.com/'))
    element1 = Element(title="বিবিসি বাংলা", image_url="https://d1yjjnpx0p53s8.cloudfront.net/styles/logo-thumbnail/s3/0023/3343/brand.gif?itok=1UXhEJs0", subtitle="খবর, সর্বশেষ খবর, ব্রেকিং নিউজ", item_url="http://bbcbangla.com/")
    element2 = Element(title="প্রথম আলো", image_url="https://d1yjjnpx0p53s8.cloudfront.net/styles/logo-thumbnail/s3/052014/prthm_aalo.jpg?itok=i7S-cVgj",subtitle="Latest online bangla news",item_url='https://www.prothomalo.com/')
    element3 = Element(title="bdnews24.com",image_url='https://d30fl32nd2baj9.cloudfront.net/media/2013/01/04/logo1.png1/BINARY/logo1.png',subtitle="Bangladesh's first bilingual 24/7 news provider in any medium opened its content to public free of charge on 23 Oct 2006",item_url="https://bdnews24.com/")
    elements.append(element1)
    elements.append(element2)
    elements.append(element3)
    bot.send_generic_message(recipient_id, elements)

def kheladhula(recipient_id):
    text = "আপডেট পেতে যেকোনো একটি সিলেক্ট কর"
    buttons = []
    button1 = Button(title='IPL', type='postback', payload='ipl2020')
    button2 = Button(title='Cricket World Cup 2019', type="web_url", url="https://www.cricketworldcup.com/")
    button3 = Button(title="FIFA World Cup 2022", type='web_url', url='https://www.fifa.com/worldcup/')
    buttons.append(button1)
    buttons.append(button2)
    buttons.append(button3)
    bot.send_button_message(recipient_id, text, buttons)

def ipl(recipient_id):
    elements = []
    elements.append(Element(title="Kolkata Knight Riders",
                            image_url='https://www.kkr.in/static-assets/waf-images/62/73/6c/0/mN4BkixqiZ.JPG',
                            subtitle=None,
                            item_url='https://www.kkr.in/'))
    element1 = Element(title="Chennai Super Kings",
                       image_url="https://upload.wikimedia.org/wikipedia/en/thumb/2/2b/Chennai_Super_Kings_Logo.svg/250px-Chennai_Super_Kings_Logo.svg.png",
                       subtitle=None,
                       item_url="https://www.chennaisuperkings.com/CSK_WEB/index.html")
    element2 = Element(title="Indian Premier League ",
                       image_url="https://www.deccanherald.com/sites/dh/files/styles/article_detail/public/articleimages/2020/10/12/iplv1-889782-1602475398.jpg?itok=RsPGmjcr",
                       subtitle=None,
                       item_url='https://www.iplt20.com/')

    elements.append(element1)
    elements.append(element2)

    bot.send_generic_message(recipient_id, elements)

def other(recipient_id):
    Text = "নিজের স্কিল ডেভেলপ করার উপায়"
    buttons = []
    button1 = Button(title='পড়াশোনার মনোযোগ বৃদ্ধির উপায়া', type='postback', payload='study')
    button2 = Button(title="লক্ষ্যে অবিচল থাকব যেভাবে",type='postback',payload='attention')
    buttons.append(button1)
    buttons.append(button2)
    bot.send_button_message(recipient_id,Text,buttons)

def send_attention(recipient_id,encoding='utf-8'):
    resp="""
    মনে রাখবা, জীবনে যে কাজই একাগ্রতার সাথে কর না কেন তোমার অচিন্তনীয় দিক থেকে বাধা আসবেই। কিন্তু সফল তুমি তখনই হবে যখন সেই বাধা আসা সত্ত্বেও তুমি প্রচেষ্টা চালিয়ে যাবা। আর হ্যাঁ, প্রতিটা সাকসেস এর পেছনেই কিন্তু রয়েছে হার্ডওয়ার্ক! :) :) :)"""
    bot.send_text_message(recipient_id,resp)

def send_study(recipient_id,encoding='utf-8'):
    resp="""পড়ার আগে যে যে কাজগুলো করবাঃ পানি খেয়ে নিতে পারো এক গ্লাস, হালকা একটু ব্যায়াম, স্মার্টফোন পাওয়ার অফ করে রুম থেকে বের করে দিবা, পড়ার ধারা ঠিক রাখবা, যেমন কঠিন সাবজেক্ট আগে শুরু করবা, ব্রেইন তখন ফুল পাওয়ারে থাকবে, মনে মনে পড়লে মন এইদিক ঐদিক চলে গেলে শব্দ করে পড়বা, ইনশা আল্লাহ কাজ হবে, :] :] :]"""
    resp1=':] :)'
    bot.send_text_message(recipient_id,resp)
if __name__ == "__main__":
    app.run()
