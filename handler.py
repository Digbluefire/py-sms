def response_handler(body, a, b, c, d):

    message = "Today we will be testing your personality.  Please answer these questions truthfully.  Ok, first question.  Are you an 'extrovert' or an 'introvert'?"
    if body == 'extrovert':
        a = a + 1
        message = "Ok so far we have that you are an extrovert.  This has eliminated half of the personalities so we are getting close!  Now are you 'sensing' or do you use your 'intuition'?"
        return message, a, b, c, d 

    elif body == 'sensing':
        b = b + 1
        message = "Ok so now we only have 4 more personalities. So are you 'thinking' or 'feeling'?"
        return message, a, b, c, d   
    
    elif body == 'thinking':
        c = c + 1
        message = "Ok so we have two more personalities left. This question will give you your personality. Now, are you 'judging' or 'perceiving'?" 
        return message, a, b, c, d       
                
    elif body == 'judging':
        d = d + 1
        message = "Ok, thank you for completing this quiz, now we will tell you your personality. Type in 'Yes' to see your personality!"
        return message, a, b, c, d         
                
    elif body == 'introvert':
        a = a + 2
        message = "Ok so far we have that you are an introvert.  This has eliminated half of the personalities so we are getting close!  Now are you 'sensing' or do you use your 'intuition'?"
        return message, a, b, c, d  
    
    elif body == 'intuition':
        b = b + 2
        message = "Ok so now we only have 4 more personalities. So are you 'thinking' or 'feeling'?"
        return message, a, b, c, d      

    elif body == 'feeling':
        c = c + 2
        message = "Ok so we have two more personalities left. This question will give you your personality. Now, are you 'judging' or 'perceiving'?"
        return message, a, b, c, d
    
    elif body == 'perceiving':
        d = d + 2
        message =  "Ok, thank you for completing this quiz, now we will tell you your personality. Type in 'Yes' to see your personality!"
        print message, a, b, c, d
        return message, a, b, c, d 
        
    elif a == 1 and b == 1 and c == 1 and d == 1:
        message = "Ok, your personality is 'The Executive'.  Here is a link to learn more about your personality https://www.16personalities.com/entp-personality"
        return message, a, b, c, d

    elif a == 1 and b == 1 and c == 1 and d == 2:
        message = "Ok, your personality is 'The Entrepeneur'.  Here is a link to learn more about your personality https://www.16personalities.com/intp-personality"
        return message, a, b, c, d

    elif a == 1 and b == 1 and c == 2 and d == 1:
        message = "Ok, your personality is 'The Consul'.  Here is a link to learn more about your personality https://www.16personalities.com/estp-personality"
        return message, a, b, c, d

    elif a == 1 and b == 1 and c == 2 and d == 2:
        message = "Ok, your personality is 'The Entertainer'.  Here is a link to learn more about your personality https://www.16personalities.com/istp-personality"
        return message, a, b, c, d
    
    elif a == 1 and b == 2 and c == 1 and d == 1:
        message = "Ok, your personality is 'The Commander'.  Here is a link to learn more about your personality https://www.16personalities.com/esfp-personality"
        return message, a, b, c, d

    elif a == 1 and b == 2 and c == 1 and d == 2:
        message = "Ok, your personality is 'The Debater'.  Here is a link to learn more about your personality https://www.16personalities.com/intj-personality"
        return message, a, b, c, d

    elif a == 1 and b == 2 and c == 2 and d == 1:
        message = "Ok, your personality is 'The Protagonist'.  Here is a link to learn more about your personality https://www.16personalities.com/estp-personality"
        return message, a, b, c, d

    elif a == 1 and b == 2 and c == 2 and d == 2:
        message = "Ok, your personality is 'The Campaigner'.  Here is a link to learn more about your personality https://www.16personalities.com/infp-personality"
        return message, a, b, c, d

    elif a == 2 and b == 1 and c == 1 and d == 1:
        message = "Ok, your personality is 'The Logistician'.  Here is a link to learn more about your personality https://www.16personalities.com/infj-personality"
        return message, a, b, c, d
    
    elif a == 2 and b == 1 and c == 1 and d == 2:
        message = "Ok, your personality is 'The Virtuoso'.  Here is a link to learn more about your personality https://www.16personalities.com/entp-personality"
        return message, a, b, c, d

    elif a == 2 and b == 1 and c == 2 and d == 1:
        message = "Ok, your personality is 'The Defender'.  Here is a link to learn more about your personality https://www.16personalities.com/intp-personality"
        return message, a, b, c, d

    elif a == 2 and b == 1 and c == 2 and d == 2:
        message = "Ok, your personality is 'The Adventurer'.  Here is a link to learn more about your personality https://www.16personalities.com/estp-personality"
        return message, a, b, c, d

    elif a == 2 and b == 2 and c == 1 and d == 1:
        message = "Ok, your personality is 'The Architect'.  Here is a link to learn more about your personality https://www.16personalities.com/istp-personality"
        return message, a, b, c, d
    
    elif a == 2 and b == 2 and c == 1 and d == 2:
        message = "Ok, your personality is 'The Logician'.  Here is a link to learn more about your personality https://www.16personalities.com/esfp-personality"
        return message, a, b, c, d

    elif a == 2 and b == 2 and c == 2 and d == 1:
        message = "Ok, your personality is 'The Advocate'.  Here is a link to learn more about your personality https://www.16personalities.com/intj-personality"
        return message, a, b, c, d

    elif a == 2 and b == 2 and c == 2 and d == 2:
        message = "Ok, your personality is 'The Mediator'.  Here is a link to learn more about your personality https://www.16personalities.com/estp-personality"
        return message, a, b, c, d

    else:
        return "Type 'q' and please start over thank you", a, b, c, d

    print message, a, b, c, d
    return message, a, b, c, d



