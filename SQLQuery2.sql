select * from ReportingStructure

select b.EmployeeName [Reportee],a.EmployeeName [Manager] from ReportingStructure a 
inner join ReportingStructure b
on a.EmployeeID = b.ManagerID
