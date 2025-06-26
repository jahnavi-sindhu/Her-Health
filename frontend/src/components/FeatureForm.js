import React, { useState } from "react";
import axios from "axios";
import "./FeatureForm.css";

function FeatureForm() {
  const [form, setForm] = useState({
    follicle_r: "",
    follicle_l: "",
    cycle_length: "",
    amh: "",
    bmi: ""
  });

  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const payload = {
        follicle_r: Number(form.follicle_r),
        follicle_l: Number(form.follicle_l),
        cycle_length: Number(form.cycle_length),
        amh: Number(form.amh),
        bmi: Number(form.bmi),
      };

      const res = await axios.post("http://localhost:5000/predict", payload);
      setResult(res.data.prediction ? "PCOS Detected" : "No PCOS");
    } catch (err) {
      alert("Error predicting");
      console.error(err);
    }
  };

  return (
    <div className="container">
      <h1 className="heading">Her Health</h1> {/* 👈 moved here */}
      <form onSubmit={handleSubmit} className="form-card">
        <div className="form-group">
          <label>Follicle No. (Right Ovary):</label>
          <input
            type="number"
            name="follicle_r"
            value={form.follicle_r}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>Follicle No. (Left Ovary):</label>
          <input
            type="number"
            name="follicle_l"
            value={form.follicle_l}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>Cycle Length (days):</label>
          <input
            type="number"
            name="cycle_length"
            value={form.cycle_length}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>AMH (ng/mL):</label>
          <input
            type="number"
            step="0.01"
            name="amh"
            value={form.amh}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>BMI:</label>
          <input
            type="number"
            step="0.1"
            name="bmi"
            value={form.bmi}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit" className="predict-btn">Predict</button>
        {result && (
          <div className={`result ${result === "PCOS Detected" ? "positive" : "negative"}`}>
            Prediction: {result}
          </div>
        )}
      </form>
    </div>
  );
}

export default FeatureForm;
