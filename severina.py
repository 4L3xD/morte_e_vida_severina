import json, sys, os
import subprocess as sp

class Severina():
    def __init__(self, name):
        try:
            memory = open(name + '.json', 'r')
        except FileNotFoundError:
            memory = open(name + '.json', 'w')
            memory.write('''[
                            ["Severina"],
                            {
                                "/oi@morte_vida_severinabot": "Olá! Qual seu nome?",
                                "/tchau@morte_vida_severinabot": "Pessoal, eu ainda estou adquirindo inteligência. Minha programadora deixou meu código aberto então você também pode contribuir. Tchau! Tchau! 🌱"
                            }
                        ]''')
            memory.close()
            memory = open(name + '.json', 'r')
        self.name = name
        self.known, self.phrases = json.load(memory)
        memory.close()
        self.historic = [None]
    
    def listen(self, phrase=None):
        return phrase.lower()

    def think(self, phrase):
        if phrase in self.phrases:
            return self.phrases[phrase]
        if phrase == '/aprende@morte_vida_severinabot':
            return 'O que você quer que eu aprenda?'
        if phrase == 'link':
            return ""
        if '/weblink@morte_vida_severinabot ' in phrase:
            platform = sys.platform
            command = phrase.replace('weblink@morte_vida_severinabot ', '')
            if 'win' in platform:
                os.startfile(command)
            if 'linux' in platform:
                try:
                    sp.Popen(command)
                except FileNotFoundError:
                    sp.Popen(['xdg-open', command])
        
        # historic
        lastPhrase = self.historic[-1]
        if lastPhrase == 'Olá! Qual seu nome?':
            name = self.getName(phrase)
            response = self.answerName(name)
            return response
        if lastPhrase == 'O que você quer que eu aprenda?':
            self.key = phrase
            return 'Digite o que eu devo responder:'
        if lastPhrase == 'Digite o que eu devo responder:':
            response = phrase
            self.phrases[self.key] = response
            self.saveMemory()
            return 'Aprendido!'
        try:
            response = str(eval(phrase))
            return response
        except:
            pass
        return 'Não entendi...'
    
    def getName(self, name):
        if 'meu nome é ' in name:
            name = name[11:]
        name = name.title()
        return name
    
    def answerName(self, name):
        if name in self.known:
            if name != 'Severina':
                phrase = 'Eaew, '
            else:
                phrase = 'E se somos Severinas iguais em tudo na vida, morreremos de morte igual, mesma morte severina.'
        else:
            phrase = 'Muito prazer, '
            self.known.append(name)
            self.saveMemory()
        return phrase + name + '!'
    
    def saveMemory(self):
        memory = open(self.name + '.json', 'w')
        json.dump([self.known, self.phrases], memory)
        memory.close()
    
    def speak(self, phrase):
        self.historic.append(phrase)