//Javascript Object

var carInfo = {
    make: 'Toyota',
    year: 1990,
    model: 'Camry',
    //
    print: function (name) {
        return `My name is ${name} & I drive a ${this.year} ${this.make} ${this.model}.`
    },
    names: ['Smith', 'James', 1, 19, 10.29, -1]
}

carInfo['year'] = 2023

for (key in carInfo){
    console.log(carInfo[key])
}


console.log(carInfo.print('James'));