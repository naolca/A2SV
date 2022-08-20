def gradingStudents(grades):
    the_news=[]
    
    for i in grades:
        if i<38:
            the_news.append(i)
        else:
            number=i
            while number%5!=0:
                number+=1
            difference=number-i
            if difference<3:
                the_news.append(number)
            else:
                the_news.append(i)
    return the_news