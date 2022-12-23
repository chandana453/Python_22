#1.Write a query to display the name ( first name and last name ) for those employees who gets more salary than the employee whose ID is 163.
# select first_name,last_name from employees
# where salary > (select salary from employees where employee_id=163)

#2.Write a query to display the name ( first name and last name ), salary, department id, job id for those employees who works in the same designation as the employee works whose id is 169.

# SELECT first_name, last_name, salary, department_id, job_id
# FROM employees
# WHERE job_id =
# (SELECT job_id FROM employees WHERE employee_id=169);

#3.Write a query to display the name ( first name and last name ), salary, department id for those employees who earn such amount of salary which is the smallest salary of any of the departments.

# select concat(first_name,last_name) as name,salary, department_id
# from employees
# where salary in (select min(salary) from employees group by department_id)

#4.Write a query to display the employee id, employee name (first name and last name ) for all employees who earn more than the average salary.

# select employee_id,concat(first_name,last_name) as name
# from employees
# where salary > (select avg(salary) from employees)

#5.Write a query to display the employee name ( first name and last name ), employee id and salary of all employees who report to Payam

# select concat(first_name,last_name) as name,employee_id,salary
# from employees
# where manager_id=(select employee_id from employees where first_name='Payam')


#6.Write a query to display the department number, name ( first name and last name ), job and department name for all employees in the Finance department.

# select e.first_name || ' ' || e.last_name as name,e.job_id,e.department_id,
# d.department_name from employees e, departments d
# where e.department_id=d.department_id
# and d.department_name='Marketing'

#7.Write a query to display all the information of an employee whose salary and reporting person id is 3000 and 121 respectively.

# select * from employees
# where salary = 3000 and manager_id = 121
#
# (or)
# SELECT * FROM employees
# WHERE(salary, manager_id) = (SELECT 3000, 121)

#8.Display all the information of an employee whose id is any of the number 134, 159 and 183.
# select * from employees
# where employee_id in (134,159,183)

#9.Write a query to display all the information of the employees whose salary is within the range 1000 and 3000.
# select * from employees where salary between 1000 and 3000


#10.Write a query to display all the information of the employees whose salary is within the range of smallest salary and 2500.
# select * from employees
# where salary between (select min(salary) from employees) and 2500


#11.Write a query to display all the information of the employees who does not work in those departments where some employees works whose id within the range 100 and 200.
# SELECT * FROM employees
# WHERE department_id NOT IN
# (SELECT department_id FROM departments WHERE manager_id BETWEEN 100 AND 200);

#12.Write a query to display all the information for those employees whose id is any id who earn the second highest salary.
# SELECT * FROM employees
# WHERE employee_id IN
# (SELECT employee_id FROM employees  WHERE salary = (SELECT MAX(salary) FROM employees
# WHERE salary < (SELECT MAX(salary) FROM employees)));

#13.Write a query to display the employee name( first name and last name ) and hiredate for all employees in the same department as Clara. Exclude Clara.

# SELECT first_name, last_name, hire_date  FROM employees
# WHERE department_id =  ( SELECT department_id  FROM employees  WHERE first_name = 'Clara')
# AND first_name <> 'Clara';

# (<> - NOT EQUAL TO)

#14.Write a query to display the employee number and name( first name and last name ) for all employees who work in a department with any employee whose name contains a T.

# select employee_id, first_name||' '||last_name as name from employees
# where department_id IN (select department_id from employees where first_name like '%T%')

#15.Write a query to display the employee number, name( first name and last name ), and salary for all employees who earn more than the average salary and who work in a department with any employee with a J in their name.

# select employee_id,first_name||' '||last_name as name,salary from employees
# where salary > (select avg(salary) from employees)
# and department_id in (select department_id from employees where first_name like '%J%')

#16. Display the employee name( first name and last name ), employee id, and job title for all employees whose department location is Toronto.

# select first_name | | ' ' | | last_name as name, employee_id, job_id from employees
# where department_id = (Select department_id from departments
# where location_id = (select location_id from locations where city='Toronto'))

#17.Write a query to display the employee number, name( first name and last name ) and job title for all employees whose salary is smaller than any salary of those employees whose job title is MK_MAN.

# SELECT employee_id,first_name,last_name, job_id FROM employees
# WHERE salary < ANY ( SELECT salary FROM employees WHERE job_id = 'MK_MAN' )

#18.Write a query to display the employee number, name( first name and last name ) and job title for all employees whose salary is smaller than any salary of those employees whose job title is MK_MAN. Exclude Job title MK_MAN.

# SELECT employee_id,first_name,last_name, job_id FROM employees
# WHERE salary < ANY ( SELECT salary FROM employees WHERE job_id = 'MK_MAN' )
# AND job_id <> 'MK_MAN';

#19.Write a query to display the employee number, name( first name and last name ) and job title for all employees whose salary is more than any salary of those employees whose job title is PU_MAN. Exclude job title PU_MAN.

# SELECT employee_id, first_name, last_name, job_id  FROM employees
# WHERE salary > ALL ( SELECT salary  FROM employees  WHERE job_id = 'PU_MAN' )
# AND job_id <> 'PU_MAN';

#20.Write a query to display the employee number, name( first name and last name ) and job title for all employees whose salary is more than any average salary of any department.

# select employee_id,first_name||' '||last_name as name,job_id from employees
# where salary > All (select avg(salary) from employees group by department_id)

#21.Write a query to display the employee name( first name and last name ) and department for all employees for any existence of those employees whose salary is more than 3700.

# SELECT first_name, last_name, department_id FROM employees
# WHERE EXISTS (SELECT * FROM employees WHERE salary >3700 );

#22.Write a query to display the department id and the total salary for those departments which contains at least one salaried employee.
# *********************GO Through Once*********************

# SELECT departments.department_id, result1.total_amt
# FROM departments,
# ( SELECT employees.department_id, SUM(employees.salary) total_amt
# FROM employees
# GROUP BY department_id) result1
# WHERE result1.department_id = departments.department_id;

#23.Write a query to display the employee id, name ( first name and last name ) and the job id column with a modified title SALESMAN for those employees whose job title is ST_MAN and DEVELOPER for whose job title is IT_PROG.
# select employee_id, first_name||' '||last_name as name,
# case job_id
# when 'ST_MAN' then 'SALESMAN'
# when 'IT_PROG' then 'DEVELOPER'
# else job_id
# END AS designation,  salary
# from employees

#24.Write a query to display the employee id, name ( first name and last name ), salary and the SalaryStatus column with a title HIGH and LOW respectively for those employees whose salary is more than and less than the average salary of all employees.

# SELECT  employee_id,  first_name, last_name,  salary AS SalaryDrawn,
# ROUND((salary -(SELECT AVG(salary) FROM employees)),2) AS AvgCompare,
# CASE  WHEN salary >=
# (SELECT AVG(salary)
# FROM employees) THEN 'HIGH'
# ELSE 'LOW'
# END AS SalaryStatus
# FROM employees;

#25.Write a query to display the employee id, name ( first name and last name ), SalaryDrawn, AvgCompare (salary - the average salary of all employees) and the SalaryStatus column with a title HIGH and LOW respectively for those employees whose salary is more than and less than the average salary of all employees.
# SELECT  employee_id,  first_name, last_name,  salary AS SalaryDrawn,
# ROUND((salary -(SELECT AVG(salary) FROM employees)),2) AS AvgCompare,
# CASE  WHEN salary >=
# (SELECT AVG(salary)
# FROM employees) THEN 'HIGH'
# ELSE 'LOW'
# END AS SalaryStatus
# FROM employees;

#26.Write a subquery that returns a set of rows to find all departments that do actually have one or more employees assigned to them.

# SELECT  department_name FROM departments
# WHERE department_id IN (SELECT DISTINCT(department_id) FROM employees);

#278.