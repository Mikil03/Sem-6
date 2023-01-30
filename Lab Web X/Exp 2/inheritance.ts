class Person {
    firstName: string;
    lastName: string;
	constructor(firstName, lastName) {
		this.firstName = firstName;
		this.lastName = lastName;
	}
}
class Employee extends Person {
    employeeID: number;
	constructor(firstName, lastName, employeID) {
		super(firstName, lastName);
        this.employeeID = employeID;        
	}
}

class Manager extends Employee{
    department :string;
    constructor(firstName, lastName, employeID, department) {
		super(firstName, lastName, employeID);
        this.department = department;        
	}
}
let manager = new Manager('Mehul','Sharma', 123, 'Sales');
console.log("Name of manager: "+manager.firstName + manager.lastName);
console.log("Emplpoyee ID: "+ manager.employeeID);
console.log("Manager's Department: "+manager.department);