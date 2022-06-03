def myFunc(e):
  return e['up']

cars = [
  {'car': 'Ford', 'up': 2005},
  {'car': 'Mitsubishi', 'up': 2000},
  {'car': 'BMW', 'up': 2019},
  {'car': 'VW', 'up': 2011}
]

cars.sort(key=myFunc)