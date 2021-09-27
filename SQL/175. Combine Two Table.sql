select FirstName, LastName, City, State
from Person left join Address
on Person.PersonId = Address.PersonId
;

--my solution:

select p.FirstName, p.LastName, a.City, a.State
from Person p left join Address a
on p.PersonId=a.PersonId

