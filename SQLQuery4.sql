SELECT * from dbo.Employees

SELECT * INTO #4 FROM dbo.Employees

SELECT * FROM #4

DELETE FROM #4
WHERE Department is NULL or FirstName ='Bob'

TRUNCATE TABLE #4

DROP TABLE #4

-- delete for deleting certain records but without where its the same as truncate which deletes all records from the table but the structure remains intact 
-- drop deletes the table entirely 