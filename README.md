# My first Repository

Copyright 2020 Lina Alkawass

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Description

Open-Source Energy System Modeling, VU 370.062: first homework assignment  
TU Wien - Summer term

Concept:
The concept is to find which companies have extra emission allowances to sell due to European Union Emissions Trading Scheme.
The European Union Emissions Trading System (EU ETS) is the first large greenhouse gas emissions trading scheme in the world. It was launched in 2005 to fight Global warming and is a major pillar of EU climate policy. Under the ’cap and trade’ principle, a maximum (cap) is set on the total amount of greenhouse gases that can be emitted by all participating installations. ’Allowances’ for emissions are then auctioned off or allocated for free and can subsequently be traded. Installations must monitor and report their CO2 emissions, ensuring they hand in enough allowances to the authorities to cover their emissions. If emission exceeds what is permitted by its allowances, an installation must purchase allowances from others. Conversely, if an installation has performed well at reducing its emissions, it can sell its leftover credits. This allows the system to find the most cost-effective ways of reducing emissions without significant government intervention.

Assumptions:
One company can be only buyer or seller, based on the amount of allowances that it requires, if the allocation is more than the company actually produces, it enters a market as a seller.
If Allocation – Emissions > 0: the company is a seller
The market price is determined. A seller sells allowances if its minimum price <= market price.
