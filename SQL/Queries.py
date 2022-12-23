#1.Write a query in SQL to display the full name (first and last name), and salary for those employees who earn below 6000.
# select first_name || ' ' || last_name as Full_Name,salary from employees where salary<6000


#2.Write a query in SQL to display the first and last_name, department number and salary for those employees who earn more than 8000.
# select first_name,last_name,department_id,salary from employees where salary>8000

#3.Write a query in SQL to display the first and last name, and department number for all employees whose last name is “McEwen”.
#select first_name,last_name,department_id from employees where last_name='McEwen'
#or
#select first_name,last_name,department_id from employees where last_name like '%McEwen';

#4.Write a query in SQL to display all the information for all employees without any department number.
# select * from employees where department_id is NULL;

#5.Write a query in SQL to display all the information about the department Marketing.
# select * from employees e,departments d
# where e.department_id=d.department_id
# and d.department_name='Marketing'


#6.Write a query in SQL to display the full name (first and last), hire date, salary, and department number for those employees whose first name does not containing the letter M and make the result set in ascending order by department number.
# select first_name || ' ' || last_name as full_name,hire_date,salary,department_id from employees
# where first_name not like '%M%'
# order by department_id asc;

#7.Write a query in SQL to display all the information of employees whose salary is in the range of 8000 and 12000 and commission is not null or department number is except the number 40, 120 and 70 and they have been hired before June 5th, 1987. Go to the editor
# select * from employees
# where salary between 8000 and 12000
# and commission_pct is not NULL
# or department_id not in (40, 120, 70)
# and hire_date < '1987-06-05'

#8.Write a query in SQL to display the full name (first and last name), and salary for all employees who does not earn any commission.
# select first_name || ' ' || last_name as full_name,salary
# from employees
# where commission_pct is NULL

#9.Write a query in SQL to display the full name (first and last), the phone number and email separated by hyphen, and salary, for those employees whose salary is within the range of 9000 and 17000. The column headings assign with Full_Name, Contact_Details and Remuneration respectively.
# select first_name || ' ' || last_name as Full_name,
# phone_number || '-' ||email as Contact_details,
# salary as Renumeration
# from employees where salary between 9000 and 17000


#10.Write a query in SQL to display the first and last name, and salary for those employees whose first name is ending with the letter m.
# select first_name,last_name,salary
# from employees
# where first_name like '%M'

#11.Write a query in SQL to display the full name (first and last) name, and salary, for all employees whose salary is out of the range 7000 and 15000 and make the result set in ascending order by the full name.
# select first_name || ' ' || last_name as full_name, salary
# from employees
# where salary not between 7000 and 15000
# order by full_name

#12.Write a query in SQL to display the full name (first and last), job id and date of hire for those employees who was hired during November 5th, 2007 and July 5th, 2009. Go to the editor
# select first_name || ' ' || last_name as full_name,job_id,hire_date
# from employees
# where hire_date between '2007-11-05' and  '2009-07-05'

#13.Write a query in SQL to display the the full name (first and last name), and department number for those employees who works either in department 70 or 90.
# select e.first_name || ' ' || e.last_name as full_name,e.department_id
# from employees as e
# WHERE department_id IN (70 , 90);

#14. Write a query in SQL to display the full name (first and last name), salary, and manager number for those employees who is working under a manager.
# select e.first_name || ' ' || e.last_name as full_name,e.salary,e.manager_id
# from employees as e
# WHERE manager_id is not NULL

#15.Write a query in SQL to display all the information from Employees table for those employees who was hired before June 21st, 2002.
# select * from employees
# where hire_date <'2002-06-21'

#16.Write a query in SQL to display the first and last name, email, salary and manager ID, for those employees whose managers are hold the ID 120, 103 or 145.
# select first_name,last_name,email,salary,manager_id
# from employees
# where manager_id in (120,103,145)

#17.Write a query in SQL to display all the information for all employees who have the letters D, S, or N in their first name and also arrange the result in descending order by salary.
# select * from employees
# where first_name like '%D%'
# or first_name like '%S%'
# or first_name like '%N%'
# order by salary desc

#18.Write a query in SQL to display the full name (first name and last name), hire date, commission percentage, email and telephone separated by '-', and salary for those employees who earn the salary above 11000 or the seventh digit in their phone number equals 3 and make the result set in a descending order by the first name.
# select first_name ||' '|| last_name as full_name,hire_date,commission_pct,
# email||'-'||phone_number,salary
# from employees
# where salary > 11000 or phone_number like '______3%'
# order by first_name desc

#19. Write a query in SQL to display the first and last name, and department number for those employees who holds a letter s as a 3rd character in their first name. Go to the editor
# select first_name, last_name, department_id
# from employees
# where first_name like '__s%'

#20.Write a query in SQL to display the employee ID, first name, job id, and department number for those employees who is working except the departments 50,30 and 80.
# select employee_id,first_name,job_id,department_id
# from employees
# where department_id not in (50,30,80)

#21.Write a query in SQL to display the employee Id, first name, job id, and department number for those employees whose department number equals 30, 40 or 90.
# select employee_id,first_name,job_id,department_id
# from employees
# where department_id in (30,40,90)

#22.Write a query in SQL to display the ID for those employees who did two or more jobs in the past.
# select employee_id from job_history
# group by employee_id
# having count(employee_id) >=2

#23.Write a query in SQL to display job ID, number of employees, sum of salary, and difference between highest salary and lowest salary for a job.
# select job_id,count(employee_id),sum(salary),(max(salary)-min(salary)) as sal_diff
# from employees
# group by job_id

#24.Write a query in SQL to display job ID for those jobs that were done by two or more for more than 300 days.
# select e.job_id
# from job_history e
# where e.end_date - e.start_date > 300 --(DOUBT)
# group  by e.job_id
# having count(e.job_id)>=2

#25.Write a query in SQL to display the country ID and number of cities in that country we have.
# select country_id, count(city) from locations
# group by country_id

#26.Write a query in SQL to display the manager ID and number of employees managed by the manager.
# select manager_id,count(employee_id)
# from employees
# group by manager_id


#27.Write a query in SQL to display the details of jobs in descending sequence on job title.
# select * from jobs
# order by job_title desc

#28. Write a query in SQL to display the first and last name and date of joining of the employees who is either Sales Representative or Sales Man.
# SELECT first_name, last_name, hire_date
# FROM employees
# WHERE job_id IN ('SA_REP', 'SA_MAN');

#29.Write a query in SQL to display the average salary of employees for each department who gets a commission percentage.
# select avg(e.salary) , e.DEPARTMENT_ID
# from employees e
# where e.COMMISSION_PCT >0
# group by e.DEPARTMENT_ID

# (or)
# select avg(e.salary)
# from employees e
# where e.COMMISSION_PCT >0


#30. Write a query in SQL to display those departments where any manager is managing 4 or more employees.
# SELECT DISTINCT department_id
# 	FROM employees
# 		GROUP BY department_id, manager_id
# 			HAVING COUNT(employee_id) >=4;

#31.Write a query in SQL to display those departments where more than ten employees work who got a commission percentage.
# select e.department_id
# from employees e
# where e.commission_pct IS NOT NULL
# group by e.department_id
# having count(e.employee_id)>10

#32.Write a query in SQL to display the employee ID and the date on which he ended his previous job.
# select employee_id , MAX(j.end_Date)
# from job_history j
# group by j.employee_id;

#33.Write a query in SQL to display the details of the employees who have no commission percentage and salary within the range 7000 to 12000 and works in that department which number is 50.
# select * from employees
# where commission_pct is NULL
# and salary between 7000 and 12000
# and department_id=50

#34.Write a query in SQL to display the job ID for those jobs which average salary is above 8000.
# SELECT job_id, AVG(salary)
#      FROM employees
#          GROUP BY job_id
#                HAVING AVG(salary)>8000;


#35.Write a query in SQL to display job Title, the difference between minimum and maximum salaries for those jobs which max salary within the range 12000 to 18000.
# select j.JOB_TITLE , j.MAX_SALARY-j.MIN_SALARY
# from jobs j
# where j.MAX_SALARY between 12000 and 18000;

#36.Write a query in SQL to display all those employees whose first name or last name starts with the letter D
# select * from employees e
# where e.first_name like 'D%' or e.last_name like 'D%'

#37.Write a query in SQL to display the details of jobs which minimum salary is greater than 9000
# select * from jobs
# where MIN_SALARY >9000;

#38.Write a query in SQL to display those employees who joined after 7th September, 1987.
# select * from employees e
# where e.hire_date > '1987-11-7'


