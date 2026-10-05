import {services,offers,gallery} from './data.js';
import {extraServices,campaigns,clients,faqItems} from './platform/catalog.js';
const seed=()=>({services:[...structuredClone(services).map(s=>({...s,status:'published',slug:s.id+'-cleaning'})),...structuredClone(extraServices)],offers:structuredClone(offers),reviews:[],gallery:structuredClone(gallery),clients:structuredClone(clients),landingPages:structuredClone(campaigns),faqs:structuredClone(faqItems),siteContent:[],campaigns:[],customers:[],notifications:[],requests:[],bookings:[],corporate:[]});
let state=seed();
// Presentation adapter only. No network, credentials or persistent customer data.
export const repository={mode:'presentation',list:kind=>state[kind]||[],get:(kind,id)=>state[kind]?.find(x=>x.id===id),
 async initialize(){},async login(){},async logout(){},async refresh(){},
 async save(kind,item){const i=state[kind].findIndex(x=>x.id===item.id);if(i<0)state[kind].push(item);else state[kind][i]={...state[kind][i],...item};return item},
 async remove(kind,id){state[kind]=state[kind].filter(x=>x.id!==id)},
 async submit(kind,item){const record={...item,id:'AM-'+crypto.randomUUID().slice(0,8).toUpperCase(),createdAt:new Date().toISOString(),status:'new',paymentStatus:'not_requested'};state[kind].push(record);let customer=state.customers.find(c=>c.phone===item.phone);if(!customer){customer={id:'customer-'+crypto.randomUUID(),name:item.name,phone:item.phone,email:item.email||'',address:item.address,createdAt:record.createdAt,marketingConsent:false};state.customers.push(customer)}record.customerId=customer.id;state.notifications.unshift({id:record.id,requestId:record.id,kind,createdAt:record.createdAt,status:'unread'});return record},
 async submitReview(item){const r={...item,id:crypto.randomUUID(),status:'pending',createdAt:new Date().toISOString()};state.reviews.push(r);return {id:r.id}},reset(){state=seed()}
};
