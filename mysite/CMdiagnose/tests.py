from django.test import TestCase
from django.urls import reverse
from .models import Body, Tongue, Person, Cases



class TestReplaceComma(TestCase):
    def test1(self):
        b=Body()
        b.general=('不得臥，健忘，虛痛')
        caselist=Cases.objects.all()
        # for case in caselist:
        #     case.case_check(b)
        # print(b.result)
        case=Cases(facts='心虛,血不足,脈左寸弱,驚悸,不得臥，健忘，虛痛,怔忡,遺精',\
            symptom='心之虛。血不足也。脈左寸必弱。其症為驚悸。為不得臥。為健忘。為虛痛。為怔忡。為遺精。',\
            solution='驚悸者。惕惕然恐。神失守也。七福飲、秘旨安神丸主之。不得臥者。思慮太過。神不藏也。歸脾\
                湯、安神定志丸主之。健忘者。心腎不交。神明不充也。歸脾湯、十補丸主之。虛痛者。似似飢。似手摭\
                    心。喜得手按。洋參麥冬湯主之。怔忡者。氣自下逆。心悸不安。歸脾湯主之。遺精者。或有夢。或無夢。心腎不固也。清心丸、十補丸主之。')
        # print(case.facts)
        case.case_check(b)
        # print(b.result)
        # print('========================')
        # print(len(caselist))
        self.assertIs((float(case.marks) > 0.33 ), True)

class TestReplacePeriod(TestCase):
    def test1(self):
        b=Body()
        b.general=('不得臥，健忘，虛痛')
        caselist=Cases.objects.all()
        # for case in caselist:
        #     case.case_check(b)
        # print(b.result)
        case=Cases(facts='心虛,血不足,脈左寸弱,驚悸,不得臥。健忘。虛痛,怔忡,遺精',\
            symptom='心之虛。血不足也。脈左寸必弱。其症為驚悸。為不得臥。為健忘。為虛痛。為怔忡。為遺精。',\
            solution='驚悸者。惕惕然恐。神失守也。七福飲、秘旨安神丸主之。不得臥者。思慮太過。神不藏也。歸脾\
                湯、安神定志丸主之。健忘者。心腎不交。神明不充也。歸脾湯、十補丸主之。虛痛者。似似飢。似手摭\
                    心。喜得手按。洋參麥冬湯主之。怔忡者。氣自下逆。心悸不安。歸脾湯主之。遺精者。或有夢。或無夢。心腎不固也。清心丸、十補丸主之。')
        # print(case.facts)
        case.case_check(b)
        # print(b.result)
        # print('========================')
        # print(case.marks)
        # print(len(caselist))
        self.assertIs((float(case.marks) > 0.33 ), True)


class TestReplacePeriod2_with_space_in_facts(TestCase):
    '''
    the last '。' created '' element should not be counted
    '''
    def test1(self):
        b=Body()
        b.general=('心實。氣滯。血痛。痰迷')
        caselist=Cases.objects.all()
        # for case in caselist:
        #     case.case_check(b)
        # print(b.result)
        case=Cases(facts='心實。氣滯。血痛。停飲。 痰迷。暑閉。蟲嚙。')

        # print(case.facts)
        case.case_check(b)
        # print(b.result)
        # print('========================')
        # print(case.marks)
        # print(len(caselist))
        self.assertIs((float(case.marks) > 0.5 ), True)

class ReverseTestReplacePeriod2_with_space_in_facts(TestCase):
    def test1(self):
        b=Body()
        b.general=('心實。氣滯。血痛。痰迷')
        caselist=Cases.objects.all()
        # for case in caselist:
        #     case.case_check(b)
        # print(b.result)
        case=Cases(facts='心實。氣滯。血痛。停飲。 痰 迷。暑閉。蟲嚙。')

        # print(case.facts)
        case.case_check(b)
        # print(b.result)
        # print('========================')
        # print(case.marks)
        # print(len(caselist))
        self.assertIs((float(case.marks) > 0.5 ), False)

class ViewTests(TestCase):
    def testview(self):
        response = self.client.get(reverse('CMdiagnose:index'))
        self.assertEqual(response.status_code, 200)

class TestCaseCheckAccuracy(TestCase):
    '''
    facts' last separator should be deleted
    '''
    def testCaseCheckAccuracy(self):
        b=Body()
        b.general=('喘')
        caselist=Cases.objects.all()
        # for case in caselist:
        #     case.case_check(b)
        # print(b.result)
        case=Cases(facts='左寸弦大',\
            symptom='心之實。邪入之也。心不受邪。其受者胞絡耳。脈左寸必弦而大。其症為氣滯。為血痛。為停飲。	為痰迷。為暑閉。為蟲嚙。')
        # print(case.facts)

        # case.case_check(b)

        factlist=[]
        factlist=[x.strip() for x in str(case.facts).replace('，', ',').replace('。', ',').split(',')]
        # print('element in 12 testing')
        # print(factlist)
        counter = 0
        for element in factlist:

            if element in b.general:
                # counter += 1
                # print('match found in 12')
                # print(counter)
                # print(element)
                # print(b.general)
                # print('match found in 12-tail')
                counter += 1

        case.marks = str(counter/len(factlist))
        if counter/len(factlist) > 0.1:
            b.result+="可能性 " +str(float(case.marks)*100) + " % \n"
            b.result+=case.symptom + "\n" 
            b.result+=case.solution + "\n"+ "\n"+ "\n"
        # print(b.result)
        # print('=========12===============')
        # print(case.marks)
        # print(len(caselist))
        self.assertIs((float(case.marks) < 0.1 ), True)


class TestCaseCheckAccuracy2(TestCase):
    '''
    mind the percentage, can be lower than 10%
    add if element != '' situation (when there is '。' at the end of the string)
    '''
    def testCaseCheckAccuracy2(self):
        b=Body()
        b.general=('目赤')
        caselist=Cases.objects.all()
        # for case in caselist:
        #     case.case_check(b)
        # print(b.result)
        case=Cases(facts='肺熱之症。脈右寸必數。其症為目赤。為鼻衄。為咽痛。為吐血。為咳嗽濃痰。為酒積。為龜胸。為小便不利。為便血',\
            symptom='肺熱之症。脈右寸必數。其症為目赤。為鼻衄。為咽痛。為吐血。為咳嗽濃痰。為酒積。為龜胸。為小便不利。為便血')
        # print('test===========13============being')
        # print(case.facts)
        
        # case.case_check(b)

        factlist=[]
        factlist=[x.strip() for x in str(case.facts).replace('其症', '').replace('之症','')\
        .replace('為', '').replace('脈必','').replace('脈','').replace('必','').replace('，', ',').replace('。', ',').split(',')]
        # print('element in 12 testing')
        # print(factlist)
        # print('test===========13============end')
        counter = 0
        for element in factlist:

            if element != '' and element in b.general:
                # counter += 1
                # print('match found in 12')
                # print(counter)
                # print(element)
                # print(b.general)
                # print('match found in 12-tail')
                counter += 1

        case.marks = str(counter/len(factlist))
        if counter/len(factlist) > 0.05:
            b.result+="可能性 " +str(float(case.marks)*100) + " % \n"
            b.result+=case.symptom + "\n" 
            b.result+=case.solution + "\n"+ "\n"+ "\n"
        # print(b.result)
        # print('=========12===============')
        # print(case.marks)
        # print(len(caselist))
        self.assertIs((float(case.marks) > 0.05 ), True)

        




