-a = raw_input('Enter currency to convert from?')
 +a = input('Enter currency to convert from?')
  a = a.upper()
  
  
 -b = raw_input('Enter currency to convert from?')
 +b = input('Enter currency to convert from?')
  b = b.upper()
  
  
 -c = float(raw_input('Enter value to convert?'))
 +c = float(input('Enter value to convert?'))
  
  url = ('http://rate-exchange.appspot.com/currency?from=%s&to=%s&q=1') % (a, b)
  print (url
