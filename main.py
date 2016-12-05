import telebot
import Algorithmia
# A dictionary --> {programming_lang :"compile command \n run command" }
prog_lang = {'C': "tcc program.c\nrprogram", "C#": "csc program.cs\n program", "C++": "gcc program.cpp\nprogram",
                 "css": "link it with html", "Haskell": "ghc -o program program.hs\n hello.exe", "HTML": "program.html",
                 "java": "javac program.java\njava program", "JavaScript": "link it to html",
                 "lua": "lua program.lua\nto run program.lua from the command line you must put the Lua bin subdirectory on the Windows search path.",
                 "objective-c": "gcc program.c\nprogram", " Perl": "perl program.pl", "PHP": "link it to html",
                 "python": "python program.py", 'R': "Rscript program.r",
                 "scala": "scalac program.scala\nscala program", "SQL": "i tried to find out,but..",
                 "swift": "swiftc program.swift\nprogram", "VB": "vbc program.vb\n program"}
bot = telebot.TeleBot("Telegram API")
@bot.message_handler(commands=['start'])
def strt(message):
    start="Hi,this bot is made mzm .Prog_bot --This bot will take input as a file or by one message a program\n\nIt will determine which programming language it is and i will give u the necessary information for compiling and running the program. "
    bot.reply_to(message,start)

@bot.message_handler(func=lambda message: True)
def cool(message):
    input=message.text
    client = Algorithmia.client('Algorithmia API')
    algo = client.algo('PetiteProgrammer/ProgrammingLanguageIdentification/0.1.3')
    language=(algo.pipe(input).result[0][0])

    send=language+'\n'+ prog_lang[language.lower()]
    bot.reply_to(message,send)
bot.polling()
#prog_lang={'C':"tcc program.c\nrprogram","C#":"csc program.cs\n program","C++":"gcc program.cpp\nprogram","CSS":"link it with html","Haskell":"ghc -o program program.hs\n hello.exe","HTML":"program.html","Java":"javac program.java\njava program","JavaScript":"link it to html","Lua":"lua program.lua\nto run program.lua from the command line you must put the Lua bin subdirectory on the Windows search path.","Objective-C":"gcc program.c\nprogram"," Perl":"perl program.pl","PHP":"link it to html","Python":"python program.py",'R':"Rscript program.r","Scala":"scalac program.scala\nscala program","SQL":"i tried to find out,but..","Swift":"swiftc program.swift\nprogram","VB":"vbc program.vb\n program"}

