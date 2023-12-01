Pin=6545
Haraaga=350
Haraa=4000
Biin=int(input('-EVCPLUS- Fadlan geli pin-kaaga(Enter pin):'))
if Pin==Biin:
    print("1. Itus haraaga")
    print('2. Kaarka ku hadalka')
    print('3. Bixi biil')
    print("4. U wareeji EVCPlus")
    print('5. Warbxin kooban')
    print('6. Salaam Bank')
    print('7. Maareynta')
    print('8. Pill payment')
else:
    print('Lambarka sirta ah waa qalad')
Next_step=int(input())
if Next_step==1:
    print('Haraagaagu waa',Haraaga,'$')
elif Next_step==2:
    print('1. Ku shubo airtime')
    print('2. Ugu shub airtime')
    print('3. MIFI packages')
    print('4. Ku shubo internet')
    print('5. Ugu shub qof kale MMT')
    airtime=int(input())
    if airtime==1:
        print('Fadlan geli lacagta')
        Lacagta=int(input())
        print('Ma hubtaa inaad lacagta ku shubatid')
        print('1. Haa')
        print('2. Maya')
        Haa_Maya=int(input())
        if Haa_Maya==1:
          print('Waa laguu gu shubay')
        else:
            if Haa_Maya==2:
                print('Waa laga noqday')
            else:
                print('Dooro lambar sax ah')
    elif airtime==2:
             print('Fadlan geli mobileka')
             Mobile=int(input())
             print('Fadlan geli lacagta')
             Lacagta=int(input())
             print('Ma hubtaa inaad',Lacagta,'ugu shubtid',Mobile)
             print('1. Haa')
             print('2. Maya')
             Haa_Maya=int(input())
             if Haa_Maya==1:
                  print('Waa laguu gu shubay')
             else:
                 if Haa_Maya==2:
                     print('Waa laga noqday')
                 else:
                      print('Dooro lambar sax ah')
    elif airtime==3:
     print('1.Ku shubo data-da MIFI')
     Mifi=int(input())
     if Mifi==1:
         print('Internet Bundle Recharge')
     
         print('1. Isbuuc(Weekly)')
         print('2. Maalinle(Daily)')
         print('3. Bille (Mifi)')
         Bundle=int(input())
         if Bundle==1:
             print('Fadlan dooro bundle ka')
        
             print('1. $5= 10 GB')
             print('2. $10= 25 GB')
             GB=int(input())
             if GB==1:
                 print('Waa laguugu shubay bundle ka $5')
             else:
                  if GB==2:
                      print('Waa laguu gu shuubay bundle ka $10')
                  else:
                     print('Lambar sax ah dooro')
         elif Bundle==2:
              print('Fadlan dooro Bundle ka')
              print('1. $1= 2GB')
              print('2. $2 = 5GB')
              GB=int(input())
              if GB==1:
                  print('Waa laguu gu shubay bundle ka  $1')
              else:
                 if GB==2:
                     print('Waa laguu gu shubay bundle ka $2')
                 else:
                     print('Dooro lambar sax ah ')
         elif Bundle==3:
               print('Fadlan dooro bundle ka')
               print('1. $20= 40 GB')
               print('2. $40= 85GB')
               print('3. $60=150GB')
               print('4. $30= Monthly Unlimit')
               GB=int(input())
               if GB==1:
                 print('Waa laguu gu shubay bundle ka $20')
               elif GB==2:
                  print(' Waa laguu gu shubay bundle ka  $40')
               elif GB==3:
                    print('Waa laguu gu shubay bundle ka $60')
               else:
                     if GB==4:
                         print('Waa laguu gu shubay bundle ka $30')
                     else:
                        print('Dooro lambar sax ah')
         else:
             print('Dooro lambar sax ah')
     else:
         print('Dooro lambar sax ah')
    elif airtime==4:
        print('Fadlan dooro lambarka ku shubeyso')
        print('1. Isbuucle(Weekly)')
        print('2. Time based packages')
        print('3. Data')
        print('4. Maalinle(Daily)')
        print('5. Bille(MiFi)')
        Mifi=int(input())
        if Mifi==1:
            print('Fadlan geli lacagta')
            Lacagta=int(input())
            print('Ma hubtaa inaad',Lacagta,'ku shubatid')
            print('1. Haa')
            print('2. Maya')
            Haa_Maya=int(input())
            if Haa_Maya==1:
                print('Waa laguu gu shubay')
            else:
                if Haa_Maya==2:
                    print('Waa laga noqday')
                else:
                     print('Dooro lambar sax ah')
        elif Mifi==2:
            print('Fadlan geli lacagta')
            Lacagta=int(input())
            print('Ma hubtaa inaad',Lacagta,'ku shubatid')
            print('1. Haa')
            print('2. Maya')
            Haa_Maya=int(input())
            if Haa_Maya==1:
                print('Waa laguu gu shubay')
            else:
                if Haa_Maya==2:
                    print('Waa laga noqday')
                else:
                     print('Dooro lambar sax ah')
        elif Mifi==3:
            print('Fadlan geli lacagta')
            Lacagta=int(input())
            print('Ma hubtaa inaad',Lacagta,'ku shubatid')
            print('1. Haa')
            print('2. Maya')
            Haa_Maya=int(input())
            if Haa_Maya==1:
                print('Waa laguu gu shubay')
            else:
                if Haa_Maya==2:
                    print('Waa laga noqday')
                else:
                     print('Dooro lambar sax ah')
        elif Mifi==4:
            print('Fadlan geli lacagta')
            Lacagta=int(input())
            print('Ma hubtaa inaad',Lacagta,'ku shubatid')
            print('1. Haa')
            print('2. Maya')
            Haa_Maya=int(input())
            if Haa_Maya==1:
                print('Waa laguu gu shubay')
            else:
                if Haa_Maya==2:
                    print('Waa laga noqday')
                else:
                     print('Dooro lambar sax ah')
        elif Mifi==5:
            print('Fadlan geli lacagta')
            Lacagta=int(input())
            print('Ma hubtaa inaad',Lacagta,'ku shubatid')
            print('1. Haa')
            print('2. Maya')
            Haa_Maya=int(input())
            if Haa_Maya==1:
                print('Waa laguu gu shubay')
            else:
                if Haa_Maya==2:
                    print('Waa laga noqday')
                else:
                     print('Dooro lambar sax ah')
        else:
            print('Dooro lambar sax ah')
    elif airtime==5:
        print('Fadlan geli mobile ka ')
        Mobile=int(input())
        print('Fadlan geli lacagta')
        Lacagta=int(input())
        print('Ma hubtaa inaad',Lacagta,'ugu shubtid',Mobile)
        print('1. Haa')
        print('2. Maya')
        Haa_Maya=int(input())
        if Haa_Maya==1:
                print('Waa laguu gu shubay')
        else:
                if Haa_Maya==2:
                    print('Waa laga noqday')
                else:
                     print('Dooro lambar sax ah')
    else:
        print('Dooro lambar sax ah')
elif Next_step==3:
    print('Fadlan dooro')
    print('1. Post paid')
    print('2. Ku iibso')
    Paid=int(input())
    if Paid==1:
         print('1. Ogow biilka')
         print('2. Bixi biil')
         print('3. Ka bixi biil')
         Biil=int(input())
         if Biil==1:
              print('Error occured, please try again later')# Waxaan ayuu isoo qoray.
         elif Biil==2:
             print('Fadlan gali lacagta')
             Lacagta=int(input())
             print('Ma hubtaa inaad bixisid bill lacagtiisu tahay:',Lacagta)
             print('1. Haa')
             print('2. Maya')
             Haa_Maya=int(input())
             if Haa_Maya==1:
                 print('Waad ka bixisay')
             else:
                 if Haa_Maya==2:
                    print('Waa laga noqday')
                 else:
                     print('Dooro lambar sax ah')
    elif paid==2:
        print('Fadlan geli aqoonsiga ganacsiga')
        ganacsiga=int(input())
        print('Fadlan geli lambarka qaansheegad-ka')
        Qaansheegadka=int(input())
        print('Ma hubtaa inaad ku iibsato qaansheegadka',Qaansheegadka,'$')
        print('1. Haa')
        print('2. Maya')
        Haa_Maya=int(input())
        if Haa_Maya==1:
            print('Waa ku iibsatay')
        else:
            if Haa_Maya==2:
                print('Waa laga noqday')
            else:
                print('Dooro lamabar sax ah')
    else:
        print('Dooro lamabar sax ah')
elif Next_step==4:
    print('Fadlan geli mobile ka')
    Mobile=int(input())
    print('Fadlan geli lacagta')
    Lacagta=int(input())
    print('Ma hubtaa inaad u wareejisid',Lacagta,"$")
    print('1. Haa')
    print('2. Maya')
    Haa_Maya=int(input())
    if Haa_Maya==1:
     print('Evc-plus Waxaad',Lacagta,"Uwareejisay Lamabarka",Mobile,'Haragaagu waa',Haraaga-Lacagta)
    else:
        if Haa_Maya==2:
            print('Waa laga noqday')
        else:
            print('Dooro lamabar sax ah')
elif Next_step==5:
 print('Wrbixin kooban')
 print('1. Last action')
 print('2. Wareejintii u dambeysey')
 print('3. Iibsashadii ugu dambeysey')
 print('4. Last 3 actions')
 print('5. Email me my actitvity')
 Warbixin=int(input())
 if Warbixin==1:
     print('Tranld: 18828201956')
     print('Details:$500 ayaad u wareejisay (613456783)') #Qeybtaan lamakark IYO LACAGTA Adiga ayey kugu xiran tahay.
     print('Taariikh: 23/11/23')
     print('18:19:58')
 elif Warbixin==2:
     print('1.Udirtay')
     print('2. Ka heshay')
     Ka=int(input())
     if ka==1:
         print('Fadlan geli lamabarka')
         Mobile=int(input())
         print('Evc-plus $1 ayaad u wareejisay',Mobile) # Qeybtaan constanat ma ahan ee waxey ku xirantahay lamabrka lasoo geliyo
     else:
         if ka==2:
             print('Fadlan geli lamabarka')
             Mobile=int(input())
             print('Evc-plus $1 ayaad u ka heshay',Mobile) # Qeybtaan constanat ma ahan ee waxey ku xirantahay lamabrka lasoo geliyo.
         else:
             print('Dooro lamabar sax ah')
 elif Warbixin==3:
        print('Fadlan geli aqoonsiga gancasiga')
        ganacsiga=int(input())
        print('Evc-plus waxaad $34 kuu u wareejisay koontada 234454') 
 elif Warbixin==4:
     print('Your mini statement has been sent as SMS to your registered mobile no')
 elif Warbixin==5:
    print("Fadlan geli Email kaaga")
    Email= int(input())
    print('Email kaaga waxba ma kuu soo dhicin')
 else:
    print('Dooro lambar sax ah')
elif Next_step==6:
    print('Salaam Bank')
    print('1. Ka wareeji Evc-plus')
    Ka_Wareeji=int(input())
    if Ka_Wareeji==1:
        print('Fadln dooro Xisaabta Bangiga')
        print('1. Salaam Sch')
        print('2. SALAAM SOMALI BANK')
        print('3. Darasalaam Bank')
        print('4.Bank Beeraha')
        Bank=int(input())
        if Bank==1:
            print('Fadlan geli account')
            account_2=int(input())
            print('Fadlan geli lacagta')
            Lacagta=int(input())
            print('Waa laguugu wareejiyay Salaam Sch')
        elif Bank==2:
            print('Fadlan geli account')
            account_2=int(input())
            print('Fadlan geli lacagta')
            Lacagta=int(input())
            print('Waa laguugu wareejiyay SALAAM SOMALI BANK')
        elif Bank==3:
             print('Fadlan geli account')
             account_2=int(input())
             print('Fadlan geli lacagta')
             Lacagta=int(input())
             print('Waa laguugu wareejiyay Darasalaam Bank')
        elif Bank==4:
             print('Fadlan geli account')
             account_2=int(input())
             print('Fadlan geli lacagta')
             Lacagta=int(input())
             print('Waa laguugu wareejiyay Bank Beeraha')
        else:
            print('Dooro lamabar sax ah')
    else:
        print('Dooro lamabar sax ah')
elif Next_step==7:
    print('Maareynta')
    print('1. Bedel lambarka sirta ah')
    print('2. Bedel luqadda')
    print('3. Wargelin Mobile Lumay')
    print('4. Lacag Xirasho')
    print('5. U celi lacag qaldantay')
    print('6. EnableMobileBanking')
    Maareynta=int(input())
    if Maareynta==1:
        print("Fadalan geli pinkaaga cusub")
        Biin=int(input())
        print('Hubi pinkaaga cusub')
        Biin2=int(input())
        if Biin2==Biin:
            print('Evc-plus: Waad ku guuleysatay in aad badasho pin-kaaga')
        else:
            print('Dooro pin sax ah')
    elif Maareynta==2:
        print('Dooro luqadda')
        print('1. English')
        print('2. Somali')
        eng=int(input())
        if eng==1 or 2:
            print('Evc-plus: Waad ku guuleysatay inaad badasho luqadda')
        else:
            print('Dooro lamabr sax ah')
    elif Maareynta==3:
        print('Fadlan geli mobileka  lumay')
        Mobile=int(input())
        print('Waa laguugu wargelinay')
    elif Maareynta==4:
        print('Fadlan geli numbar-ka khalad-ka ah')
        Mobile=int(input())
        print('Waa laguugu xiray')
    elif Maareynta==5:
        print('Fadlan geli aqoonsiga lacag diridda')
        Aqoonsi=int(input())
        print('Fadlan geli Lamarka ')
        Mobile=int(input())
        print('Waa loo celiyey')
    elif Maareynta==6:
        print('Fadlan geli lambarka isdiwaan gelinta')
        Mobile=int(input())
        print('Subscriber <7276132> is already activated')
    else:
        print('Dooro lambar sax ah')
elif Next_step==8:
    print('Bill Payment')
    print('1. Itus haraaga')
    print('2. Wada bixi biil-ka')
    print('3. Qayb ka bixi biil-ka')
    Biil=int(input())
    if Biil==1:
        print( 'Haraagaagu waa', Haraa)
    elif Biil==2:
        print('Fadlan geli reffrance number')
        Mobile=int(input())
        print('Waad wada bixisay')
    else:
        if Biil==3:
            print('Fadlan geli reffrance number')
            Mobile=int(input())
            print('Qeyb ayaad ka bixisay')
        else:
            print('Dooro lambar sax ah')
else:
    print('Dooro lambar sax ah')
            


        
        
 



        
            
    
      
    
        
           

         
    



