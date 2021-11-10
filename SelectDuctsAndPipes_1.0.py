"""
Этот скрипт выбирает все воздуховоды и трубы в проекте Revit. Создайте нод Python Script в пустом проекте Dynamo и вставьте туда этот код
"""

import clr # Модуль для подгрузки .NET библиотек

# Библиотеки Revit API
clr.AddReference('RevitAPI') # Основная библиотека Revit API
from Autodesk.Revit.DB import * # Импорт всех классов
from Autodesk.Revit.DB.Mechanical import Duct # Импорт класса воздуховодов
from Autodesk.Revit.DB.Plumbing import Pipe # Импорт класса труб

# Библиотеки Dynamo
clr.AddReference('RevitServices') # Работа с документом и транзакциями
from RevitServices.Persistence import DocumentManager as DM

# Системные библиотеки
import System # Работа с системными типами и структурами данных .NET
from System import Type # Импорт класса Type, необходимого для создания типизированного списка классов
from System.Collections.Generic import List # Импорт класса типизированного списка

doc = DM.Instance.CurrentDBDocument # Получение файла документа

types = [FamilyInstance, Duct, Pipe] # Создание списка необходимых классов
typeList = List[Type]() # Создание пустого типизированного списка c типом данных Type (класс)

for t in types: # Создание цикла для добавления классов в типизированный список
	typeList.Add(t) # Добавляем элементы в типизированный список методом Add

# Создание фильтра. Меняем False на True, если надо исключить элементы, а не оставить их в коллекторе
filter = ElementMulticlassFilter(typeList,False)
# Получение элементов на активном виде с примененным фильтром по нескольким классам
elems = FilteredElementCollector(doc,doc.ActiveView.Id).WherePasses(filter).ToElements()

OUT = elems