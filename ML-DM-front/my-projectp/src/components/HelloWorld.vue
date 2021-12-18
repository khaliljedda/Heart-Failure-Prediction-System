<template>
  <div>
    <br /><br /><br /><br />

    <b-card>
      <h3>Medical analysis content</h3>
      <br />
      <div class="row m-2">
        <div class="col-4">
          
          <b-form-input
            v-model="data.Age"
            placeholder="Age"
            type="number"
          ></b-form-input>
        </div>
        <div class="col-4">
          
          <b-form-select
          class="from-control"
            v-model="data.Sex"
            placeholder="Sex"
            :options="OptionSex"
          ></b-form-select>
        </div>
        <div class="col-4">
          <b-form-select
            :options="OptionC"
            v-model="data.ChestPainType"
            placeholder="ChestPainType"
            type="text"
          ></b-form-select>
        </div>
      </div>
      <div class="row m-2">
        <div class="col-4">
          <b-form-input
            v-model="data.Cholesterol"
            placeholder="Cholesterol"
            type="text"
          ></b-form-input>
        </div>
        <div class="col-4">
          <b-form-select
          :options="OptionF"
            v-model="data.FastingBS"
            placeholder="FastingBS"
            type="text"
          ></b-form-select>
        </div>
        <div class="col-4">
          <b-form-select
          :options="OptionR"
            v-model="data.RestingECG"
            placeholder="RestingECG"
            type="text"
          ></b-form-select>
        </div>
      </div>
      <div class="row m-2">
        <div class="col-4">
          <b-form-input
            v-model="data.MaxHR"
            placeholder="MaxHR"
            type="text"
          ></b-form-input>
        </div>
        <div class="col-4">
          <b-form-select
            v-model="data.ExerciseAngina"
            :options="OptionE"
            placeholder="ExerciseAngina"
            type="text"
          ></b-form-select>
        </div>
        <div class="col-4">
          <b-form-input
            v-model="data.Oldpeak"
            placeholder="Oldpeak"
            type="text"
          ></b-form-input>
        </div>
      </div>

      <div class="row m-2">
        <div class="col-4">
          <b-form-select
            v-model="data.ST_Slope"
            :options="OptionS"
            placeholder="ST_Slope"
            type="text"
          ></b-form-select>
        </div>
        <div class="col-4"></div>
      </div>
    </b-card>
    <br />b
    <b-button variant="danger" class="ml-atuo" @click="result"
      >Estimate death danger</b-button
    >
    <br />
    <br />
    <br /><br /><br />
    <b-card>
      <h3 style="float: left">Death danger</h3>
      <br />
      <br />
      <div class="row">
        <Avancement :value="Math.round(rst * 100)" class="col-8"></Avancement>
        <div class="col-4"><strong>resultat</strong>: {{ rst }}</div>
      </div>
    </b-card>
  </div>
</template>

<script>
import axios from "axios";
import Avancement from "./Avancement.vue";

export default {
  components: {
    Avancement,
    
  },
  data() {
    return {
      OptionSex: [
        {
          value: "Female",
          text: "Female",
        },
         {
          value: "Male",
          text: "Male",
        },
      ],
       OptionC: [
        {
          value: "ATA",
          text: "ATA",
        },
         {
          value: "NAP",
          text: "NAP",
        },
         {
          value: "TA",
          text: "TA",
        },
         {
          value: "ASY",
          text: "ASY",
        },
      ],
       OptionF: [
        {
          value: "0",
          text: "0",
        },
         {
          value: "1",
          text: "1",
        },
       
      ],

       OptionR: [
        {
          value: "Normal",
          text: "Normal",
        },
         {
          value: "ST",
          text: "ST",
        },
         {
          value: "LVH",
          text: "LVH",
        },
       
      ],

      OptionE:[ 
        {
          value: "N",
          text: "N",
        },
         {
          value: "Y",
          text: "Y",
        },
        ],

         OptionS:[ 
        {
          value: "Up",
          text: "Up",
        },
         {
          value: "Flat",
          text: "Flat",
        },  {
          value: "Down",
          text: "Down",
        },
        ],
      rst: 0.1,
      data: {
        Age: 40,
        Sex: "Male",
        ChestPainType: "ATA",
        RestingBP: 140,
        Cholesterol: 289,
        FastingBS: 0,
        RestingECG: "Normal",
        MaxHR: 172,
        ExerciseAngina: "N",
        Oldpeak: 0,
        ST_Slope: "Up"
      },
    };
  },

  methods: {
    result() {
      axios
        .post("http://127.0.0.1:5000/predict_api", this.data)
        .then((res) => {
          this.rst = res.data.result;
        })
        .catch((error) => {
          console.log(error);
        })
        .finally(() => {
          //Perform action in always
        });
    },
  },
};
</script>