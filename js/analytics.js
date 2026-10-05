// Integration contract for a later implementation. Presentation sends no tracking data.
let attribution={};
export function captureAttribution(){const q=new URLSearchParams(location.search);if(!attribution.landingPage||q.has('utm_campaign'))attribution={landingPage:location.pathname,...Object.fromEntries(['utm_source','utm_medium','utm_campaign','utm_content','utm_term'].map(k=>[k,(q.get(k)||'').slice(0,150)]))};return {...attribution}}
export function track(){}
export function pageView(){captureAttribution()}
export function enableAnalytics(){return false}
