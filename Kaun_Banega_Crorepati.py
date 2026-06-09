questions = [["According to a popular Hindi saying, what is it that does not grow on trees?","Flowers","Fruits","Money","Leaves","Money",1000],
             ["Which of these cities is famously known across India as the \"Pink City\"?","Bengaluru","Mysore","Jaipur","Kochi","Jaipur",2000],
             ["Who is the composer of India's National Anthem, \"Jana Gana Mana\"?","Bankim Chandra Chattopadhyay","Rabindranath Tagore","Lal Bahadur Shastri","R.K. Narayan","Rabindranath Tagore",3000],
             ["In Kalidasa's classic play, which rishi, known for his extreme temper, cursed Shakuntala that she would be forgotten by her lover?","Rishi Durvasa","Rishi Vishwamitra","Rishi Agastya","Rishi Vashistha","Rishi Durvasa",5000],
             ["Which of these specific water bodies completely surrounds the island territory of Diu?","Bay of Bengal","Arabian Sea","Indian Ocean","Laccadive Sea","Arabian Sea",10000],
             ["According to the Valmiki Ramayana, which rishi's intense wrath burned the 60,000 sons of King Sagara to ashes?","Rishi Atri","Rishi Vishwamitra","Rishi Kapila","Rishi Durvasa","Rishi Kapila",20000],
             ["Who was the first sportsperson to be honored with India's highest sporting award, the Rajiv Gandhi Khel Ratna (now Major Dhyan Chand Khel Ratna), in 1992?","Sachin Tendulkar","Viswanathan Anand","Geet Sethi","Leander Peas","Viswanathan Anand",40000],
             ["Among these individuals, whom does the Indian Constitution explicitly permit to take part in the active proceedings of Parliament without being a member?","Solicitor General","Attorney General","Cabinet Secretary","Chief Justice of India","Attorney General",80000],
             ["Who was just 11 years and 10 months old when she became the youngest Indian to ever compete at the Olympic Games back in 1952?","Nilima Ghose","Mary D'Souza","Arati Saha","Dolly Nazir","Aarti Saha",160000],
             ["In 1982, Dr. Barney Clark became the first historic recipient of a permanently implanted artificial heart. What was this medical device named?","Liotta Heart","Abo Cor Heart","Jarvik 7 Heart","Akutsu III Heart","Jarvik 7 Heart",320000],
             ["Which was the very first aircraft to be prominently featured on a postage stamp issued in independent India?","Lockheed Constellation","Douglas DC-4","Westland Wapiti","Humber-Sommer Monoplane","Lockheed Constellation",640000],
             ["Which rock band, whose music albums Indian astronaut Kalpana Chawla had carried with her into space, wrote the instrumental song \"Contact Lost\" to honor the deceased Columbia crew?","Pink Floyd","Deep Purple","Black Sabbath","Green Day","Deep Purple",1250000],
             ["Who won the inaugural edition of the historic Durand Cup football tournament when it was first held in Simla in 1888?","Highland Light Infantry","Royal Irish Rifles","Royal Scots Fusiliers","East York Regiment","Royal Scott Fusiliers",2500000],
             ["Who invented the world's first commercial stock ticker machine in the year 1867?","Edward Calahan","Thomas Edison","David Gestetner","Robert Barclay","Edward Calahan",5000000],
             ["Who was the Indian bowler off whom the Australian cricket legend Sir Don Bradman scored a single run to reach his monumental 100th first-class century?","Baqa Jilani","Commandur Rangachari","Gogumal Kishenchand","Kanwar Rai Singh","Gogumal Kishenchand",10000000],
             ["Which Japanese artist visited India in the 1930s and painted a highly celebrated woodblock series depicting landscapes of the Taj Mahal, the Sanchi Stupa, and the Ellora Caves?","Hiroshi Sugimoto","Hiroshi Senju","Hiroshi Yoshida","Hiroshi Nakajima","Hiroshi Yoshida"],70000000]
price_money=0
for i in range(1,len(questions)+1,1):
    print(f"Question {i} is right in front of your computer screen :-\n{questions[i-1][0]}\nAnd options are :-\nOption 1 :- {questions[i-1][1]}\nOption 2 :- {questions[i-1][2]}\nOption 3 :- {questions[i-1][3]}\nOption 4 :- {questions[i-1][4]}")
    if i==1:
        ans=int(input("Type the option number which you want to choose :- "))
        if questions[i-1][5]==questions[i-1][ans]:
            print(f"Yay! You are right and you have won {questions[i-1][6]} rupees\nKeep Going!!")
        else:
            print("Damn! You are wrong and you have to leave without a penny")
    else:
        print("Do you want to continue or quit")
        progress=int(input("Press 1 to continue or 0 to quit :- "))
        if progress==1:
            ans=int(input("Type the option number which you want to choose :- "))
            if i>1 and i<=5:
                if questions[i-1][5]==questions[i-1][ans]:
                    print(f"Yay! You are right and you have won {questions[i-1][6]} rupees till now\nKeep Going!!")
                else:
                    print("Damn! You are wrong and you have to leave without a penny")
            elif i>=6 and i<=10:
                if questions[i-1][5]==questions[i-1][ans]:
                    print(f"Yay! You are right and you have won {questions[i-1][6]} rupees till now\nKeep Going!!")
                else:
                    print("Damn! You are wrong and you have to leave with an amount of 10000 rupees")
            elif i>=11 and i<=15:
                if questions[i-1][5]==questions[i-1][ans]:
                    print(f"Yay! You are right and you have won {questions[i-1][6]} rupees till now\nKeep Going!!")
                else:
                    print("Damn! You are wrong and you have to leave with an amount of 320000 rupees")
            else:
                if questions[i-1][5]==questions[i-1][ans]:
                    print(f"Yay! You are right and you have won {questions[i-1][6]} rupees\nThe Game ends!!!")
                else:
                    print("Damn! You committed a blunder\nNow you have to leave the game with only 320000 rupees only")
        elif progress==0:
            print(f"So now you have to leave the game with an amount of {price_money}")
            break
    price_money=questions[i-1][6]