package com.example.controller;
import org.springframework.stereotype.Controller; 
import org.springframework.web.bind.annotation.RequestMapping; 
import org.springframework.web.bind.annotation.ResponseBody; 
@Controller
public class HarnessController {
	@RequestMapping("/") 
    @ResponseBody
    public String hello() 
    { 
        return "Welcome"; 
    }
	@RequestMapping("/index") 
    @ResponseBody
    public String index() 
    { 
        return "This is index page"; 
    }
}
