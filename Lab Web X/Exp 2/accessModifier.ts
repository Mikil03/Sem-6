class Student{
public name :string = "Mikil";
protected roll :number = 37;
private accNo :number = 12345;
getAccNo()
{
    return this.accNo;
}
}

class Person extends Student{
    constructor()
    {
        super();
    }
    display()
    {
        return "Roll number of student: "+this.roll;
    }
}

let s :Student = new Student();
let p :Person = new Person();

console.log("Name of student: "+s.name);
console.log(p.display());
console.log("Account number of student: "+s.getAccNo());