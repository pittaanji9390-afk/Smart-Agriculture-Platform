/**
 * Mandi Market Intelligence & Farm Economics Module
 */

async function fetchMandiPrices() {
    try {
        const res = await fetch("/api/market/prices");
        const data = await res.json();
        renderMandiTable(data.market_items);
        renderTopGainers(data.top_gainers);
    } catch (err) {
        console.error("Failed to load mandi prices", err);
    }
}

function renderMandiTable(items) {
    const tableBody = document.getElementById("mandi-table-body");
    if (!tableBody) return;
    tableBody.innerHTML = "";

    items.forEach(item => {
        const isUp = item.price_change_pct >= 0;
        const row = document.createElement("tr");
        row.className = "border-b border-slate-800 text-xs hover:bg-slate-800/40 transition";
        row.innerHTML = `
            <td class="py-3 px-3 font-semibold text-slate-100">${item.commodity}</td>
            <td class="py-3 px-3 text-slate-300">${item.market_name}, <span class="text-slate-400">${item.state}</span></td>
            <td class="py-3 px-3 font-bold text-emerald-400">₹${item.modal_price_rs_per_quintal.toLocaleString()}</td>
            <td class="py-3 px-3 text-slate-400">₹${item.min_price} - ₹${item.max_price}</td>
            <td class="py-3 px-3 font-bold ${isUp ? 'text-emerald-400' : 'text-red-400'}">
                ${isUp ? '▲ +' : '▼ '}${item.price_change_pct}%
            </td>
        `;
        tableBody.appendChild(row);
    });
}

function renderTopGainers(gainers) {
    const container = document.getElementById("top-gainers-container");
    if (!container) return;
    container.innerHTML = "";

    gainers.forEach(g => {
        const card = document.createElement("div");
        card.className = "p-3 bg-emerald-950/20 border border-emerald-800/30 rounded-xl flex items-center justify-between";
        card.innerHTML = `
            <div>
                <p class="text-xs font-semibold text-slate-200">${g.commodity}</p>
                <p class="text-[11px] text-slate-400">${g.market_name}</p>
            </div>
            <div class="text-right">
                <p class="text-xs font-bold text-emerald-400">₹${g.modal_price_rs_per_quintal}</p>
                <p class="text-[10px] font-semibold text-emerald-300">▲ +${g.price_change_pct}%</p>
            </div>
        `;
        container.appendChild(card);
    });
}

function calculateFarmProfit() {
    const acreage = parseFloat(document.getElementById("profit-acres").value) || 1.0;
    const yieldPerAcre = parseFloat(document.getElementById("profit-yield").value) || 20.0; // Quintals
    const pricePerQtl = parseFloat(document.getElementById("profit-price").value) || 2500.0;
    const inputCostPerAcre = parseFloat(document.getElementById("profit-cost").value) || 15000.0;

    const totalYield = acreage * yieldPerAcre;
    const grossRevenue = totalYield * pricePerQtl;
    const totalCost = acreage * inputCostPerAcre;
    const netProfit = grossRevenue - totalCost;
    const roi = totalCost > 0 ? (netProfit / totalCost) * 100 : 0;

    document.getElementById("res-gross-rev").textContent = `₹${Math.round(grossRevenue).toLocaleString()}`;
    document.getElementById("res-total-cost").textContent = `₹${Math.round(totalCost).toLocaleString()}`;
    document.getElementById("res-net-profit").textContent = `₹${Math.round(netProfit).toLocaleString()}`;
    document.getElementById("res-roi").textContent = `${Math.round(roi)}%`;
}
