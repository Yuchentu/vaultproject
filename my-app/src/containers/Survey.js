import React, { Component } from "react";
import "./Survey.css";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      selectedOption1: "option1",
      selectedOption2: "option1",
      selectedOption3: "option1"
    };
  }

  handleFormSubmit = formSubmitEvent => {
  formSubmitEvent.preventDefault();

  };


  handleOptionChange1 = changeEvent => {
    this.setState({
      selectedOption1: changeEvent.target.value
    });
  };
  handleOptionChange2 = changeEvent => {
    this.setState({
      selectedOption2: changeEvent.target.value
    });
  };
  handleOptionChange3 = changeEvent => {
    this.setState({
      selectedOption3: changeEvent.target.value
    });
  };

  render() {
    return (
      <div className="Survey">
        <form onSubmit={this.handleFormSubmit}>
        <p> Question 1 </p>
          <div className="form-check">
            <label>
              <input
                type="radio"
                name="question-1"
                value="option1"
                checked={this.state.selectedOption1 === "option1"}
                onChange={this.handleOptionChange1}
                className="form-check-input"
              />
              Choice 1
            </label>
          </div>

          <div className="form-check">
            <label>
              <input
                type="radio"
                name="question-1"
                value="option2"
                checked={this.state.selectedOption1 === "option2"}
                onChange={this.handleOptionChange1}
                className="form-check-input"
              />
              Choice 2
            </label>
          </div>

          <div className="form-check">
            <label>
              <input
                type="radio"
                name="question-1"
                value="option3"
                checked={this.state.selectedOption1 === "option3"}
                onChange={this.handleOptionChange1}
                className="form-check-input"
              />
              Choice 3
            </label>
          </div>
          <div>
          <p> Question 2 </p>
          </div>
          <div className="form-check">
            <label>
              <input
                type="radio"
                name="question-2"
                value="option1"
                checked={this.state.selectedOption2 === "option1"}
                onChange={this.handleOptionChange2}
                className="form-check-input"
              />
              Choice 1
            </label>
          </div>

          <div className="form-check">
            <label>
              <input
                type="radio"
                name="question-2"
                value="option2"
                checked={this.state.selectedOption2 === "option2"}
                onChange={this.handleOptionChange2}
                className="form-check-input"
              />
              Choice 2
            </label>
          </div>

          <div className="form-check">
            <label>
              <input
                type="radio"
                name="question-2"
                value="option3"
                checked={this.state.selectedOption2 === "option3"}
                onChange={this.handleOptionChange2}
                className="form-check-input"
              />
              Choice 3
            </label>
          </div>
          <p> Question 3 </p>
          <div className="form-check">
            <label>
              <input
                type="radio"
                name="question-3"
                value="option1"
                checked={this.state.selectedOption3 === "option1"}
                onChange={this.handleOptionChange3}
                className="form-check-input"
              />
              Choice 1
            </label>
          </div>

          <div className="form-check">
            <label>
              <input
                type="radio"
                name="question-3"
                value="option2"
                checked={this.state.selectedOption3 === "option2"}
                onChange={this.handleOptionChange3}
                className="form-check-input"
              />
              Choice 2
            </label>
          </div>

          <div className="form-check">
            <label>
              <input
                type="radio"
                name="question-3"
                value="option3"
                checked={this.state.selectedOption3 === "option3"}
                onChange={this.handleOptionChange3}
                className="form-check-input"
              />
              Choice 3
            </label>
          </div>
          <div className="form-group">
            <button className="btn btn-primary mt-2" type="submit">
              Save
            </button>
          </div>
        </form>
      </div>
    );
  }
}

export default App;

