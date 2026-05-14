document.querySelector("form").addEventListener("submit", function (e) {
    e.preventDefault();
    calculate();
});

function parseIP(ip) {
    const parts = ip.trim().split(".");
    if (parts.length !== 4) return null;
    const nums = parts.map(Number);
    if (nums.some(n => isNaN(n) || n < 0 || n > 255)) return null;
    return nums;
}

function parseMask(mask) {
    mask = mask.trim();

    if (/^\/?\d{1,2}$/.test(mask)) {
        const prefix = parseInt(mask.replace("/", ""));
        if (prefix < 0 || prefix > 32) return null;
        return cidrToOctets(prefix);
    }

    const parts = parseIP(mask);
    if (!parts) return null;

    const bin = parts.map(o => o.toString(2).padStart(8, "0")).join("");
    if (!/^1*0*$/.test(bin)) return null;

    return parts;
}

function cidrToOctets(prefix) {
    const bin = "1".repeat(prefix) + "0".repeat(32 - prefix);
    return [0, 8, 16, 24].map(i => parseInt(bin.slice(i, i + 8), 2));
}

function octetsToPrefix(mask) {
    return mask.map(o => o.toString(2).padStart(8, "0")).join("").split("0")[0].length;
}

function ipToInt(octets) {
    return ((octets[0] << 24) | (octets[1] << 16) | (octets[2] << 8) | octets[3]) >>> 0;
}

function intToIP(n) {
    return [(n >>> 24) & 255, (n >>> 16) & 255, (n >>> 8) & 255, n & 255].join(".");
}

function getClass(ip) {
    const first = ip[0];
    if (first >= 1 && first <= 126) return "A";
    if (first === 127) return "A (loopback)";
    if (first >= 128 && first <= 191) return "B";
    if (first >= 192 && first <= 223) return "C";
    if (first >= 224 && first <= 239) return "D (multicast)";
    if (first >= 240 && first <= 254) return "E (reserved)";
    return "—";
}

function setField(id, value) {
    document.getElementById(id).value = value;
}

function showError(message) {
    ["networkaddr", "class", "broadcast", "addressnum", "ipsusable", "firstusable", "lastusable"]
        .forEach(id => setField(id, ""));
    alert(message);
}

function calculate() {
    const ipRaw = document.getElementById("ipaddr").value;
    const maskRaw = document.getElementById("mask").value;

    const ip = parseIP(ipRaw);
    if (!ip) {
        showError("Neplatná IP adresa. Zadejte ve formátu např. 192.168.1.10");
        return;
    }

    const mask = parseMask(maskRaw);
    if (!mask) {
        showError("Neplatná maska sítě. Zadejte ve formátu 255.255.255.0 nebo /24");
        return;
    }

    const ipInt   = ipToInt(ip);
    const maskInt = ipToInt(mask);
    const wildInt = (~maskInt) >>> 0;

    const networkInt   = (ipInt & maskInt) >>> 0;
    const broadcastInt = (networkInt | wildInt) >>> 0;

    const totalAddresses = wildInt + 1;
    const usableAddresses = totalAddresses > 2 ? totalAddresses - 2 : 0;

    const prefix = octetsToPrefix(mask);

    setField("networkaddr",  intToIP(networkInt) + " /" + prefix);
    setField("class",        getClass(ip));
    setField("broadcast",    intToIP(broadcastInt));
    setField("addressnum",   totalAddresses.toLocaleString("cs-CZ"));
    setField("ipsusable",    usableAddresses > 0 ? usableAddresses.toLocaleString("cs-CZ") : "žádné");
    setField("firstusable",  usableAddresses > 0 ? intToIP(networkInt + 1)   : "—");
    setField("lastusable",   usableAddresses > 0 ? intToIP(broadcastInt - 1) : "—");
}