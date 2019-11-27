from SeleniumBuiltins.db import getEmpDetails,insertEmp


insertEmp("INSERT INTO Employee  VALUES (1004, 'Teju', 'sharma', 'Delhi','Bangalore','Python');")
getEmpDetails("SELECT * from Employee;")