"""
6208. [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 5. 객체지향 2
국적을 출력하는 printNationality 정적 메서드를 갖는 Korean 클래스를 정의하고
 

메서드를 호출하는 코드를 작성해봅시다.


출력


대한민국

대한민국


"""
shit


class Country():

   
    def __init__(self, countryname):
        self.countryname = countryname

    @staticmethod
    def two_countries(self, countryname):
        return f'{self.countryname}\n{self.countryname}'



class Korea:
    countryname = '대한민국'

print(Country.two_countries(Country, countryname))
