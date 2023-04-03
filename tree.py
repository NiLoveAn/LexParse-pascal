from parser import build_tree

data = '''
program abs;
var
  x, y, z: integer;

begin
  while 2 > 1 do begin
    x := 10;  //xz xz xz
    x := 11;
    end;
  
if x > 5 then begin
    z := x * y;
    if z > x then begin
      break;
      end;
    end;

for i := 1 to 2 do begin
    x := x + 1;
    y := x + 5;
    end;
  
  writeln(x);
  writeln(y);
  writeln(z);
end.
'''

result = build_tree(data)
print (result)


#S = " "
#with open('test.pas', 'r') as reader:
#    S += reader.read()
#result = build_tree(S)
#print (result)
