import kivy  
import time
from kivy.app import App  
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.config import Config
from kivy.uix.textinput import TextInput 
from kivy.uix.label import Label
from kivy.core.window import Window

Config.set('graphics', 'resizable', True)
 



class SpanishConjactor(App):
    def build(self):
         
        Window.clearcolor = (0,0,.1,9) 

        global rl

        rl = RelativeLayout(size =(300, 300))
        
        Noun_lable = Label(text ="Noun",
                           pos_hint ={'center_x':.5, 'center_y':.9} 
                           )
        
        self.Noun = TextInput(font_size = 20, 
                      size_hint =(.4, None), 
                      height = 40,
                      pos_hint ={'center_x':.5, 'center_y':.8},
                      )
        
        Verb_lable = Label(text ="Verb",
                           pos_hint ={'center_x':.5, 'center_y':.7} 
                           )

        self.Verb = TextInput(font_size = 20, 
                      size_hint =(.4, None), 
                      height = 40,
                      pos_hint ={'center_x':.5, 'center_y':.6},
                      )

        All_Enter = Button(size_hint =(.3, .1),  
                    text ="All Enter",
                    pos_hint ={'center_x':.5, 'center_y':.3}
                        )
        All_Enter.bind(on_press = self.all_cal)

        global output_lable

        output_lable = Label(text = '',
                        pos_hint ={'center_x':.5, 'center_y':.2}, 
                        )
        

        
        
        rl.add_widget(output_lable)
        rl.add_widget(self.Verb)
        rl.add_widget(Verb_lable)
        rl.add_widget(Noun_lable)
        rl.add_widget(self.Noun)
        rl.add_widget(All_Enter)
        return rl
        
        
    
    
    
    
    def all_cal(self, obj):
        print("" + self.Noun.text) 
        print("" + self.Verb.text)
        
        kbam = 1
        string = self.Verb.text
        lst = []
 
        for letter in string:
            lst.append(letter)
 
        print(lst)
   
        sup = 0
        res = ''
        c = self.Noun.text
        b = self.Verb.text
        a = [b]
        d = lst
        cat = len(d)
        dog = cat - 2
        rabbit = d[dog] 
        global output

        if c == 'Yo':
            for i in d:
                sup += 1
                res += i
                if sup == dog:
                    res = res + 'o'
                    output = res
                    print(res)
                    break
        elif c == 'Tu' and rabbit == 'e':
            for i in d:
                sup += 1
                res += i
                if sup == dog:
                    res = res + 'es'
                    output = res
                    print(res)
                    break
        elif c == 'Tu' and rabbit == 'a':
            for i in d:
                sup += 1
                res += i
                if sup == dog:
                    res = res + 'as'
                    output = res
                    print(res)
                    break
        elif c == 'Tu' and rabbit == 'i':
            for i in d:
                sup += 1
                res += i
                if sup == dog:
                    res = res + 'es'
                    output = res
                    print(res)
                    break
        elif c == 'Ella' or c == 'El' or c == 'Ud.'and rabbit == 'a':
            for i in d:
                sup += 1
                res += i
                if sup == dog:
                    res = res + 'a'
                    output = res
                    print(res)
                    break  
        elif c == 'Ella' or c == 'El' or c == 'Ud.'and rabbit == 'i':
            for i in d:
                sup += 1
                res += i
                if sup == dog:
                    res = res + 'e'
                    output = res
                    print(res)
                    break
        elif c == 'Ella' or c == 'El' or c == 'Ud.'and rabbit == 'e':
            for i in d:
                sup += 1
                res += i
                if sup == dog:
                    res = res + 'e'
                    output = res
                    print(res)
                    break
        elif c == 'Nosotros' and rabbit == 'e':
            for i in d:
                sup += 1
                res += i
                if sup == dog:
                    res = res + 'emos'
                    output = res
                    print(res)
                    break
        elif c == 'Nosotros' and rabbit == 'a':
            for i in d:
                sup += 1
                res += i
                if sup == dog:
                    res = res + 'amos'
                    output = res
                    print(res)
                    break
        elif c == 'Nosotros' and rabbit == 'i':
            for i in d:
                sup += 1
                res += i
                if sup == dog:
                    res = res + 'imos'
                    output = res
                    print(res)
                    break
        elif c == 'Ellas' or c == 'Ellos' or c == 'Uds.'and rabbit == 'e':
            for i in d:
                sup += 1
                res += i
                if sup == dog:
                    res = res + 'en'
                    output = res
                    print(res)
                    break
        elif c == 'Ellas' or c == 'Ellos' or c == 'Uds.'and rabbit == 'i':
            for i in d:
                sup += 1
                res += i
                if sup == dog:
                    res = res + 'en'
                    output = res
                    print(res)
                    break
        elif c == 'Ellas' or c == 'Ellos' or c == 'Uds.'and rabbit == 'a':
            for i in d:
                sup += 1
                res += i
                if sup == dog:
                    res = res + 'an'
                    output = res
                    print(res)
                    break
        
        output_lable.text = output

            
        
        return rl

if __name__ == "__main__":
    SpanishConjactor().run()