# Dadata_API
Программа для доступа к сервису Dadata и получения точных координат введенного адреса.

В программе есть 2 файл - main и sql_lite.
Main  содержит в себе основной код, sql_lite функции по созданию и работе с базой данных.

Программа работает с сервисом Dadata через API. Для доступа Вам необхолдимо зарегистрироваться на сайте https://dadata.ru/.
В личном кабинете будут лоступны API-ключ и секретный ключ необходимые для работы с программой.

Запустите файла main. Программа запросит у Вас API-ключ и секретный ключ, а так же спросит на каком языке выдавать запрос. Сейчас доступно 2 языка- русский и английский.

После ввода ключей необходимо ввести адрес. Если вы не помните точный адрес, то можно ввести город и улицу, программа предложит вам то, что найдет максимально близкое к Вашему запросу.
На выходе Вы получите список адресов, из которых нужно будет выбрать конкретный и по данному адресу будет выведена информация о широте и долготе, а так же почтовый индекс и регион.
