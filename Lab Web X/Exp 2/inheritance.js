var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var Person = /** @class */ (function () {
    function Person(firstName, lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }
    return Person;
}());
var Employee = /** @class */ (function (_super) {
    __extends(Employee, _super);
    function Employee(firstName, lastName, employeID) {
        var _this = _super.call(this, firstName, lastName) || this;
        _this.employeeID = employeID;
        return _this;
    }
    return Employee;
}(Person));
var Manager = /** @class */ (function (_super) {
    __extends(Manager, _super);
    function Manager(firstName, lastName, employeID, department) {
        var _this = _super.call(this, firstName, lastName, employeID) || this;
        _this.department = department;
        return _this;
    }
    return Manager;
}(Employee));
var manager = new Manager('Mehul', 'Sharma', 123, 'Sales');
console.log("Name of manager: " + manager.firstName + manager.lastName);
console.log("Emplpoyee ID: " + manager.employeeID);
console.log("Manager's Department: " + manager.department);
