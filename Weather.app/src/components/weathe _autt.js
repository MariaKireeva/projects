import React from "react";
import './weather_autt.css'


class WeatheAutt extends React.Component{

    //let icon = this.props.date.weather.map(item) => (item.icon);

    render(){
        let icon = this.props?.api?.current?.weather?.map((item) => item.icon);
        return (
            <div className="current">
            { this.props.city &&
            <div>
                <div className="current__city">
                 {this.props.city}
                </div>
                <img className="current__img"
                src={`https://openweathermap.org/img/wn/${icon}@4x.png`}
                alt= {this.props?.api?.current?.weather.map((item) => item.description)}
                />
                
                <div className="current__temp">
                    <div className="current__temp--text">Температура:</div>
                    <div className="current__temp--item">{this.props.temp}&deg;C</div> 
                </div>
                <div className="current__descriptions"> 
                   <div className="current__descriptions--text">описание:</div> 
                   <div className="current__descriptions--item">{this.props?.api?.current?.weather.map((item) => item.description)}</div>
                </div>
               
                <div className="current__pressure">
                    <div className="current__pressure--text">Давление:</div>
                    <div className="current__pressure--item">{this.props.pressure}</div>
                </div>


             </div>
            }
            </div>
        );
    }
}

export default WeatheAutt