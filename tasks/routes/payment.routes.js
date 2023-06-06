import { Router } from "express";
import { createSession } from "../controllers/pay.controller.js"


const router = Router();

router.post('/create-checkout-session', createSession);

router.get('/sucess', (req,res) => res.send("success"));

router.get('/cancel', (req, res) => res.send("cancel"));


export default router;