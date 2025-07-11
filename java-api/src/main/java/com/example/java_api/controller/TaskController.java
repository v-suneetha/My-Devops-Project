package com.example.java_api.controller;

import org.springframework.web.bind.annotation.*;

import java.util.*;

@RestController
@RequestMapping("/tasks")
public class TaskController {

    public Map<Integer, String> tasks = new HashMap<>();
    public int index=1;

    public TaskController() {
        tasks.put(index++, "Learn Java");
        tasks.put(index++, "Learn Spring Boot");
        tasks.put(index++, "Practice DevOps");
    }

    @GetMapping
    public Map<Integer, String> getTasks() {
        return tasks;
    }

    // GET /tasks/{id} → Returns task by ID
    @GetMapping("/{id}")
    public String getTaskById(@PathVariable int id) {
        if (tasks.containsKey(id)) {
            return tasks.get(id);
        } else {
            return "Task not found";
        }
    }

    @PostMapping
    public String AddTask(@RequestBody String newTask)
    {
        tasks.put(index++, newTask);
        return  "Task added successfully" + "\nid: "+ index + "Task: " + newTask;
    }
}

