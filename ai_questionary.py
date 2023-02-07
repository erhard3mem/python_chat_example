import time
import turtle

erhard = turtle.Turtle();

def speak_rect(str):
    for i in range(len(str)):
        #print(str[i],end=" ");        
        erhard.write(str[i])
        erhard.fd(8);
        time.sleep(0.01);
        #on position 90 turn 90°, on position 180 turn 90°
        if(i/90>=1 and i%90==0):
            erhard.rt(90);
    erhard.rt(90);
    erhard.fd(20);


def speak_bubble(str):
    for i in range(len(str)):
        #print(str[i],end=" ");        
        erhard.write(str[i])
        erhard.fd(10);
        erhard.rt(1);
        time.sleep(0.01);
        #on position 90 turn 90°, on position 180 turn 90°
        #if(i/90>=1 and i%90==0):
        #    erhard.rt(90);    
    erhard.fd(20);

speak_rect('Colleague: Maybe just a basic question. But what i see from the last lectures is: that you can not trust an AI that it will give you the correct output or result? Maybe there is a high chance (95% or higher) but never a 100% chance. At least when it comes to machine learning and label data correct. Are there methods to detect such wrong output or at the end a human is needed to verify the output?');

speak_bubble('Myself helping: This is a basic problem. AI can only calculate in 0 and 1s on transistor level. If you describe the solution in percentages ("numbers" being able to processes by normal processing units) you can calculate a result with a computer, maybe see.')

erhard.fd(30);

speak_rect('I will try to give another example, if I am your professor and my eye muscle is damaged, and by the help of artificial intelligence I can give you an answer, it is not said, that you will have the motiviation to study the answer next hand, so what remains in your memory is always around 100%');


turtle.mainloop();