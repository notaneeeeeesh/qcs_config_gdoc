import{d,y as p,u as t,t as n,l as o,m as c,v as u,I as f,J as l,G as _,K as w}from"./index-C93ZdGCA.js";const g={class:"m-3 flex flex-row items-center justify-center"},b=d({__name:"Login",setup(x){function r(a){let e=new FormData(a.target);l.login.submit({email:e.get("email"),password:e.get("password")})}return(a,e)=>{const s=o("Input"),i=o("Button"),m=o("Card");return c(),p("div",g,[t(m,{title:"Login to your FrappeUI App!",class:"w-full max-w-md mt-4"},{default:n(()=>[u("form",{class:"flex flex-col space-y-2 w-full",onSubmit:w(r,["prevent"])},[t(s,{required:"",name:"email",type:"text",placeholder:"johndoe@email.com",label:"User ID"}),t(s,{required:"",name:"password",type:"password",placeholder:"••••••",label:"Password"}),t(i,{loading:f(l).login.loading,variant:"solid"},{default:n(()=>e[0]||(e[0]=[_("Login")])),_:1},8,["loading"])],32)]),_:1})])}}});export{b as default};
