import React from "react";



class Form extends React.Component{
    

    render(){
        return (
            <form onSubmit= {this.props.weatherMetod} className="form" >
                <div className="select">
                <select className ="select_city"  name="city" >
                    <option >Выберете город</option>
                    <option value="London" >Лондон</option>
                    <option value="Moscow">Москва</option>
                    <option value="Kiev">Мадрид</option>
                    <option value="Warshawa">Минск</option>
                  </select>
                  
                
                  <select className="select_exclude" name="exclude" >
                    <option >Какая погода вас интересует</option>
                    <option value="current">Текущая</option>
                    <option value="daily">На 7 дней</option>
                    <option value="hourly">Ближайшие два дня </option>
                  </select>
                  </div>
                
                <div className ="button">
                <button className="btn"> Показать погоду </button>
                </div>
                
            </form>
        );
    }
}

export default Form