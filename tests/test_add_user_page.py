from typing import Union

import pytest

from pages.add_user_page import AddUserPage
class TestAddUserPage:

    ''' Так отсутствует документация с требованиями, зададим свои :)
        Почта: 1) Обязательно должен быть символ "@" и домен после него (только protei.ru) 2) Наличие букв (от 3-х) перед "@"
        3) Отсутствие спец. символов кроме "_" 4) Миниум 5 (макс 12) символов до @ 5) Только En раскладка
        Пароль: 1) от 6 до 16 символов, 2) должен иметь хотя-бы 1 цифру и 1 спец. символ
        Имя: 1) Полностью на одном языке, 2) без спец. символов 3) без чисел 4) все символы в нижнем регистре, кроме 1 буквы
        (может быть в нижнем тоже)
        '''

    @pytest.mark.parametrize('email,password,name,gender,r_button,check_box',[('student_235@protei.ru','Maxim_364','Ilya','Мужской',1,2),
                                                                                   ('studenti236@protei.ru',"Максим#вц3","Дарья",'Женский',1,[3,2]),
                                                                                   ('stud@protei.ru',"abraca324da%bra","кирилл",'Мужской',1,[1,2,3]),
                                                                                   ('student23_8@protei.ru',"Кукари_2ку","Ruslana",'Женский',1,None),
                                                                                   ('studentka2_38@protei.ru', "Никилик333#","евдоким", 'Мужской', 2, 3) ,
                                                                                   ('studentys@protei.ru', "1_a$345dfсшылсм","Polina", 'Женский', 2, [1,3]),
                                                                                   ('studak@protei.ru', "1_2звgggmb126780","Ванечек", 'Мужской', 2, [1,2,3]),
                                                                                   ('adslos2@protei.ru', "Kybokd()2","Юлия", 'Женский', 2, None),
                                                                                   ('skl22_3@protei.ru', "paro_6","Igor", 'Мужской', 2, 2),
                                                                                   ('studakplstnb@protei,ru', "1_2звgggmb126780","Natasha", 'Женский', 1, 1),
                                                                                    ('   adjlock2@protei,ru', "Klikod()2","Михаил", 'Мужской', 2, 1)
                                                                                     ])

    def test_valid_create_user(self,init_driver,email,password,name,gender,r_button:Union[str,int],
                         check_box:Union[str,int,list,tuple,set,None]):
        add_user_page = AddUserPage(init_driver)
        add_user_page.open_url('http://185.67.95.60/add_user')
        assert add_user_page.create_user(email,password,name,gender,r_button,check_box) == True

    def test_duplicate_create_user(self,init_driver):
        add_user_page = AddUserPage(init_driver)
        add_user_page.open_url('http://185.67.95.60/add_user')
        add_user_page.create_user('kornishon@protei.ru','212_выйвsауйыx','Кирилл',"Мужской",2,None)
        add_user_page.open_url('http://185.67.95.60/add_user')
        assert add_user_page.create_user('kornishon@protei.ru','212_выйвsауйыx','Кирилл',"Мужской",2,None) == False

    @pytest.mark.parametrize('email,password,name,gender,r_button,check_box',[('student_235 @protei.ru','Maxim_7774','Ilya','Мужской',1,3),
                                                                              ('s222_d@protei.ru','[dsdsnвтоца23','Karolina','Женский',1,[1,3]),
                                                                              ('stu_dent_235','Милдзавыхdvw','Егор','Мужской',1,[1,2,3]),
                                                                              ('','213_вцйь+23','Юлия','Женский',2,[2,3]),
                                                                              ('_#*','Gorgeeai%(3)','Arkadi','Мужской',2,None),
                                                                              ('90235@protei.ru','__3__2_dsd','Nikita','Мужской',1,None),
                                                                              ('студент@protei.ru','Maxim_36423239','Monika','Женский',1,2),
                                                                              ('st_klpor5_s2s@protei.ru','McCEVKIN_364','Seva','Мужской',2,1),
                                                                              ('sklm5n@protei.ru'*16,'Никилswd$3','Илья','Мужской',2,[1,2,3]),
                                                                              (5555849,'Pompa_r4mpa','Влада','Женский',2,[1,2,3]),
                                                                              ('__@_$_#','vOkpla3@33','Veronika','Женский',2,[1,2,3]),
                                                                              ('studentka@protei,ru','Maxim_364333','Владимир','Мужской',2,[1,2,3])
                                                                              ])
    def test_incorrect_email(self,init_driver,email,password,name,gender,r_button:Union[str,int],
                         check_box:Union[str,int,list,tuple,set,None]):
        add_user_page = AddUserPage(init_driver)
        add_user_page.open_url('http://185.67.95.60/add_user')
        assert  add_user_page.create_user(email,password,name,gender,r_button,check_box) == False

    @pytest.mark.parametrize('email,password,name,gender,r_button,check_box',
                             [('student_11000@protei.ru', 'i_23'*64, 'Mikola', 'Женский', 1, 3),
                              ('student23231_8@protei.ru', '', 'Николай', 'Мужской', 1, [1, 3]),
                              ('stu_dent_235@protei.ru', 'ки*2'*4+'ъ', "Катя",'Женский', 2, None),
                              ('s90235std@protei.ru', 'Ma4i_', 'Petr', 'Мужской', 1, None),
                              ('studak2228@protei.ru', '###__(*$&', 'Diana', 'Женский', 1, 2),
                              ('st_kls2s@protei.ru', 843493364, 'Александр', 'Мужской', 2, 1),
                              ('kolyaNikol@protei.ru', 'Maxim_364', 'Александра', 'Женский', 2, [1, 2, 3])
                              ])
    def test_incorrect_password(self, init_driver, email, password, name, gender, r_button: Union[str, int],
                             check_box: Union[str, int, list, tuple, set, None]):
        add_user_page = AddUserPage(init_driver)
        add_user_page.open_url('http://185.67.95.60/add_user')
        assert add_user_page.create_user(email, password, name, gender, r_button, check_box) == False

    @pytest.mark.parametrize('email,password,name,gender,r_button,check_box',
                             [('student_235 @protei.ru', 'Maxim_7774','Анд_рей', 'Мужской', 1, 3),
                              ('s222_d@protei.ru', 'pass&word2','Nik lay', 'Мужской', 1, [1, 3]),
                              ('stu_dent_235', 'Maxim_364', '', 'Мужской', 1, [1, 2, 3]),
                              ('studak2228@protei.ru', 'Maxim_364', 278374, 'Мужской', 2, [2, 3]),
                              ('studak2228@protei.ru', 'Maxim_364', 'ЛеШа', 'Мужской', 2, [2, 3]),
                              ('studak2228@protei.ru', 'Maxim_364', 'Andрей', 'Мужской', 2, [2, 3]),
                              ])
    def test_incorrect_name(self, init_driver, email, password, name, gender, r_button: Union[str, int],
                                check_box: Union[str, int, list, tuple, set, None]):
        add_user_page = AddUserPage(init_driver)
        add_user_page.open_url('http://185.67.95.60/add_user')
        assert add_user_page.create_user(email, password, name, gender, r_button, check_box) == False

