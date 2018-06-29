from schema import Schema, Use, And, Or

Schema(int).validate(10)

Schema(int).validate('10')

Schema([int]).validate([1,2,3])

Schema({'a':int, 'b':float}).validate({'a':10,'b':20.5})

Schema([{'a':int, 'b':float}]).validate([{'a':10,'b':20.5},{'a':3,'b':20.5}])

Schema(Use(lambda x: x > 10)).validate(10)

Schema(Use(int)).validate(10)

Schema(And(Use(lambda x: x <= 10), int)).validate(4.5)


Schema(Or(int, float)).validate(1.0)